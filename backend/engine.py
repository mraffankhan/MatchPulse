"""
Hybrid Resume-Job Matching Engine.
Combines:
1. Sublinear TF-IDF + Latent Semantic Analysis (LSA) dense cosine similarity.
2. Domain Skill Taxonomy & Exact/Fuzzy matching with gap matrix.
3. Experience duration and Seniority level alignment.
4. Education degree matching.
5. Actionable ATS optimization recommendations and tailored bullet suggestions.
"""

import math
import re
from typing import Dict, Any, List, Set
import numpy as np

from .taxonomy import SENIORITY_RANKS, EDUCATION_LEVELS


class HybridMatcher:
    """Core intelligence engine for calculating multi-dimensional candidate-job fit."""

    STOPWORDS: Set[str] = {
        "a", "about", "above", "after", "again", "against", "all", "am", "an", "and", "any", "are",
        "aren't", "as", "at", "be", "because", "been", "before", "being", "below", "between", "both",
        "but", "by", "can't", "cannot", "could", "couldn't", "did", "didn't", "do", "does", "doesn't",
        "doing", "don't", "down", "during", "each", "few", "for", "from", "further", "had", "hadn't",
        "has", "hasn't", "have", "haven't", "having", "he", "he'd", "he'll", "he's", "her", "here",
        "here's", "hers", "herself", "him", "himself", "his", "how", "how's", "i", "i'd", "i'll", "i'm",
        "i've", "if", "in", "into", "is", "isn't", "it", "it's", "its", "itself", "let's", "me", "more",
        "most", "mustn't", "my", "myself", "no", "nor", "not", "of", "off", "on", "once", "only", "or",
        "other", "ought", "our", "ours", "ourselves", "out", "over", "own", "same", "shan't", "she",
        "she'd", "she'll", "she's", "should", "shouldn't", "so", "some", "such", "than", "that", "that's",
        "the", "their", "theirs", "them", "themselves", "then", "there", "there's", "these", "they",
        "they'd", "they'll", "they're", "they've", "this", "those", "through", "to", "too", "under",
        "until", "up", "very", "was", "wasn't", "we", "we'd", "we'll", "we're", "we've", "were", "weren't",
        "what", "what's", "when", "when's", "where", "where's", "which", "while", "who", "who's", "whom",
        "why", "why's", "with", "won't", "would", "wouldn't", "you", "you'd", "you'll", "you're", "you've",
        "your", "yours", "yourself", "yourselves"
    }

    @classmethod
    def tokenize(cls, text: str) -> List[str]:
        """Clean and tokenize text, preserving programming symbols like c++, c#, .net."""
        # Normalize text but preserve # and +
        text_lower = text.lower()
        # Replace punctuation except +, #, and alphanumeric
        tokens = re.findall(r"[a-z0-9+#]+(?:\.[a-z0-9]+)*", text_lower)
        # Filter stop words and single short character non-skills
        meaningful = [t for t in tokens if t not in cls.STOPWORDS and (len(t) > 1 or t in ["c", "r"])]
        return meaningful

    @classmethod
    def generate_ngrams(cls, tokens: List[str], n: int = 2) -> List[str]:
        """Generate bi-grams or tri-grams for phrase semantics."""
        return [" ".join(tokens[i:i+n]) for i in range(len(tokens) - n + 1)]

    @classmethod
    def compute_tfidf_and_lsa_similarity(cls, doc1: str, doc2: str) -> float:
        """
        Compute hybrid TF-IDF + Latent Semantic Analysis (LSA) dense cosine similarity
        using pure NumPy without external library dependencies.
        """
        tokens1 = cls.tokenize(doc1)
        tokens2 = cls.tokenize(doc2)

        if not tokens1 or not tokens2:
            return 0.0

        # Include unigrams and bigrams
        all_terms1 = tokens1 + cls.generate_ngrams(tokens1, 2)
        all_terms2 = tokens2 + cls.generate_ngrams(tokens2, 2)

        # Build combined vocabulary
        vocab = sorted(list(set(all_terms1 + all_terms2)))
        vocab_idx = {term: i for i, term in enumerate(vocab)}
        V = len(vocab)

        if V == 0:
            return 0.0

        # Count frequencies
        vec1 = np.zeros(V, dtype=np.float64)
        vec2 = np.zeros(V, dtype=np.float64)

        for t in all_terms1:
            vec1[vocab_idx[t]] += 1.0

        for t in all_terms2:
            vec2[vocab_idx[t]] += 1.0

        # Sublinear TF scaling: 1 + log(tf) if tf > 0 else 0
        pos1 = vec1 > 0
        if np.any(pos1):
            vec1[pos1] = 1.0 + np.log(vec1[pos1])

        pos2 = vec2 > 0
        if np.any(pos2):
            vec2[pos2] = 1.0 + np.log(vec2[pos2])

        # Document Frequency for IDF
        df = (vec1 > 0).astype(np.float64) + (vec2 > 0).astype(np.float64)
        # Smooth IDF: log((N + 1) / (DF + 1)) + 1
        idf = np.log(3.0 / (df + 1.0)) + 1.0

        vec1_tfidf = vec1 * idf
        vec2_tfidf = vec2 * idf

        # Base Cosine Similarity
        norm1 = np.linalg.norm(vec1_tfidf)
        norm2 = np.linalg.norm(vec2_tfidf)

        if norm1 == 0 or norm2 == 0:
            base_cos = 0.0
        else:
            base_cos = float(np.dot(vec1_tfidf, vec2_tfidf) / (norm1 * norm2))

        # Latent Semantic Analysis (SVD) dense semantic enhancement
        # Construct 2 x V term matrix
        term_matrix = np.vstack([vec1_tfidf, vec2_tfidf])
        try:
            # Perform SVD to extract latent contextual concepts
            u, s, vt = np.linalg.svd(term_matrix, full_matrices=False)
            # Reconstructed low-rank latent representation
            latent1 = u[0] * s
            latent2 = u[1] * s
            l_norm1 = np.linalg.norm(latent1)
            l_norm2 = np.linalg.norm(latent2)
            if l_norm1 > 0 and l_norm2 > 0:
                lsa_cos = float(np.dot(latent1, latent2) / (l_norm1 * l_norm2))
                # Soft blend: 70% direct TF-IDF cosine + 30% latent concept similarity
                combined = 0.7 * base_cos + 0.3 * max(0.0, lsa_cos)
            else:
                combined = base_cos
        except Exception:
            combined = base_cos

        return round(float(np.clip(combined, 0.0, 1.0)), 4)

    @classmethod
    def calculate_skill_match(
        cls, resume_skills: List[Dict[str, str]], job_skills: List[Dict[str, str]]
    ) -> Dict[str, Any]:
        """
        Compare candidate skills with job requirements, classifying into:
        - Matched Skills
        - Missing Critical Skills
        - Candidate Bonus Skills
        - Domain-by-Domain breakdown
        """
        resume_skill_names = {s["name"].lower(): s for s in resume_skills}
        job_skill_names = {s["name"].lower(): s for s in job_skills}

        matched = []
        missing = []
        bonus = []

        # Find matching and missing
        for name_lower, skill_info in job_skill_names.items():
            if name_lower in resume_skill_names:
                matched.append(skill_info)
            else:
                missing.append(skill_info)

        # Find bonus skills
        for name_lower, skill_info in resume_skill_names.items():
            if name_lower not in job_skill_names:
                bonus.append(skill_info)

        total_required = len(job_skills)
        matched_count = len(matched)

        if total_required == 0:
            score = 100.0 if matched_count > 0 else 75.0
        else:
            score = (matched_count / total_required) * 100.0

        # Domain breakdown
        domain_stats = {}
        for skill in job_skills:
            cat = skill["category"]
            if cat not in domain_stats:
                domain_stats[cat] = {"required": 0, "matched": 0}
            domain_stats[cat]["required"] += 1

        for skill in matched:
            cat = skill["category"]
            if cat in domain_stats:
                domain_stats[cat]["matched"] += 1

        domain_breakdown = []
        for cat, stats in domain_stats.items():
            pct = round((stats["matched"] / stats["required"]) * 100, 1) if stats["required"] > 0 else 0
            domain_breakdown.append({
                "domain": cat,
                "required": stats["required"],
                "matched": stats["matched"],
                "match_percentage": pct
            })

        return {
            "score": round(min(score, 100.0), 1),
            "matched_skills": sorted(matched, key=lambda x: x["name"]),
            "missing_skills": sorted(missing, key=lambda x: x["name"]),
            "bonus_skills": sorted(bonus, key=lambda x: x["name"]),
            "total_required": total_required,
            "matched_count": matched_count,
            "domain_breakdown": domain_breakdown
        }

    @classmethod
    def calculate_experience_match(cls, candidate_yrs: float, required_yrs: float) -> Dict[str, Any]:
        """Calculate alignment between candidate experience and job requirement."""
        if required_yrs <= 0:
            score = 100.0
            status = "Experience requirement satisfied (or none specified)"
        elif candidate_yrs >= required_yrs:
            # Full score with bonus recognition
            score = 100.0
            diff = round(candidate_yrs - required_yrs, 1)
            status = f"Exceeds requirement by {diff} year(s)" if diff > 0 else "Exactly meets required years"
        else:
            # Proportional score
            ratio = candidate_yrs / required_yrs
            score = max(round(ratio * 100.0, 1), 20.0)
            diff = round(required_yrs - candidate_yrs, 1)
            status = f"Short by {diff} year(s)"

        return {
            "score": round(score, 1),
            "candidate_years": candidate_yrs,
            "required_years": required_yrs,
            "status": status
        }

    @classmethod
    def calculate_seniority_match(cls, candidate_level: str, required_level: str) -> Dict[str, Any]:
        """Calculate alignment between seniority levels."""
        c_rank = SENIORITY_RANKS.get(candidate_level.lower(), 3)
        r_rank = SENIORITY_RANKS.get(required_level.lower(), 3)

        if c_rank >= r_rank:
            score = 100.0
            status = "Seniority matches or exceeds target role"
        elif c_rank == r_rank - 1:
            score = 80.0
            status = "Close seniority level (Potential promotion target)"
        else:
            score = 55.0
            status = "Lower seniority level than specified"

        return {
            "score": score,
            "candidate_seniority": candidate_level,
            "required_seniority": required_level,
            "status": status
        }

    @classmethod
    def calculate_education_match(cls, candidate_edu: str, required_edu: str) -> Dict[str, Any]:
        """Calculate alignment between education levels."""
        c_rank = EDUCATION_LEVELS.get(candidate_edu.lower(), 2)
        r_rank = EDUCATION_LEVELS.get(required_edu.lower(), 2)

        if r_rank <= 2:  # Not strictly specified
            score = 100.0
            status = "Education requirement satisfied"
        elif c_rank >= r_rank:
            score = 100.0
            status = "Degree meets or exceeds requirement"
        elif c_rank == r_rank - 1:
            score = 75.0
            status = "Equivalent qualification or minor degree gap"
        else:
            score = 50.0
            status = "Formal degree criteria gap"

        return {
            "score": score,
            "candidate_education": candidate_edu,
            "required_education": required_edu,
            "status": status
        }

    @classmethod
    def generate_recommendations(
        cls, missing_skills: List[Dict[str, str]], resume_data: Dict[str, Any], job_data: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Generate high-impact ATS recommendations and tailored resume bullet points."""
        recs = []

        # 1. Missing Critical Keywords
        if missing_skills:
            top_missing = [s["name"] for s in missing_skills[:5]]
            recs.append({
                "type": "critical_keywords",
                "title": "Incorporate High-Priority Missing Skills",
                "description": f"The job description explicitly mentions: {', '.join(top_missing)}. Adding these to your skills section and bullet points will significantly increase ATS scan rates.",
                "action": "Add relevant experience or coursework featuring these keywords.",
                "impact": "High"
            })

            # Generate tailored bullet point suggestions
            bullet_suggestions = []
            for skill in missing_skills[:4]:
                skill_name = skill["name"]
                cat = skill.get("category", "")
                if "Frontend" in cat:
                    suggestion = f"Engineered scalable user interfaces utilizing {skill_name}, resulting in a 25% improvement in page load speed and enhanced user engagement."
                elif "Backend" in cat or "Database" in cat:
                    suggestion = f"Architected high-throughput RESTful/microservices using {skill_name}, reducing API latency by 40% under peak load."
                elif "Cloud" in cat or "DevOps" in cat:
                    suggestion = f"Streamlined deployment pipelines and infrastructure with {skill_name}, boosting release cadence by 3x and achieving 99.9% uptime."
                elif "AI" in cat or "Data" in cat:
                    suggestion = f"Implemented predictive machine learning pipelines with {skill_name}, increasing model accuracy by 18% on production datasets."
                else:
                    suggestion = f"Leveraged {skill_name} within cross-functional agile teams to deliver key features on schedule with zero production regressions."

                bullet_suggestions.append({
                    "skill": skill_name,
                    "suggested_bullet": suggestion
                })

            recs.append({
                "type": "tailored_bullets",
                "title": "Suggested Tailored Bullet Points",
                "description": "Copy and customize these accomplishment-driven bullet points for your experience section:",
                "bullets": bullet_suggestions,
                "impact": "High"
            })

        # 2. Section Completeness Check
        sections = resume_data.get("sections", {})
        missing_sections = []
        for sec in ["summary", "skills", "experience", "education"]:
            if not sections.get(sec):
                missing_sections.append(sec.title())

        if missing_sections:
            recs.append({
                "type": "formatting",
                "title": "Missing Standard Resume Sections",
                "description": f"ATS parsers look for standard headers. Your resume appears to be missing: {', '.join(missing_sections)}.",
                "action": "Add clear, standard section headings so automated ATS systems don't discard your application.",
                "impact": "Medium"
            })

        # 3. Measurable Metrics Check
        raw_text = resume_data.get("raw_text", "")
        metrics_found = len(re.findall(r"\b\d+%\b|\$\d+|\b\d+x\b|\b\d+\s*(?:million|k|thousand|users)\b", raw_text, re.IGNORECASE))
        if metrics_found < 3:
            recs.append({
                "type": "impact_metrics",
                "title": "Quantify Achievements with Data",
                "description": "Recruiters and modern matching algorithms favor resumes with quantifiable impact (percentages, dollar amounts, time saved, user growth).",
                "action": "Rewrite bullet points following the 'Accomplished [X] as measured by [Y], by doing [Z]' formula.",
                "impact": "Medium"
            })

        # 4. Length check
        word_count = resume_data.get("word_count", 0)
        if word_count < 250:
            recs.append({
                "type": "content_depth",
                "title": "Resume May Be Too Brief",
                "description": f"Your resume contains {word_count} words. Highly competitive tech resumes typically contain 450 - 900 words to adequately demonstrate depth.",
                "action": "Expand on project responsibilities, technologies utilized, and team collaborations.",
                "impact": "Medium"
            })
        elif word_count > 1500:
            recs.append({
                "type": "content_depth",
                "title": "Resume May Exceed Optimal Length",
                "description": f"Your resume contains {word_count} words. Consider condensing older roles to keep the resume crisp (ideally 1–2 pages).",
                "action": "Focus on the most recent 5 years of relevant achievements.",
                "impact": "Low"
            })

        return recs

    @classmethod
    def match(cls, resume_data: Dict[str, Any], job_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute full multi-dimensional hybrid matching between parsed resume and job description.
        """
        # 1. Semantic / LSA TF-IDF Similarity
        semantic_sim = cls.compute_tfidf_and_lsa_similarity(
            resume_data.get("raw_text", ""), job_data.get("raw_text", "")
        )
        if semantic_sim <= 0:
            semantic_score = 0.0
        else:
            semantic_score = round(min(100.0, (semantic_sim ** 0.6) * 155.0), 1)

        # 2. Skill Taxonomy Match
        skill_res = cls.calculate_skill_match(
            resume_data.get("skills", []), job_data.get("skills", [])
        )
        skill_score = skill_res["score"]

        # 3. Experience Match
        exp_res = cls.calculate_experience_match(
            resume_data.get("experience_years", 0.0), job_data.get("required_years", 0.0)
        )
        exp_score = exp_res["score"]

        # 4. Seniority Match
        sen_res = cls.calculate_seniority_match(
            resume_data.get("seniority_level", "Mid-Level"), job_data.get("required_seniority", "Mid-Level")
        )
        sen_score = sen_res["score"]

        # 5. Education Match
        edu_res = cls.calculate_education_match(
            resume_data.get("education_level", "Not Specified"), job_data.get("required_education", "Not Specified")
        )
        edu_score = edu_res["score"]

        # Weighted Composite Score Calculation
        # Skills: 45%, Semantic: 30%, Experience & Seniority: 20%, Education: 5%
        composite_score = (
            (skill_score * 0.45) +
            (semantic_score * 0.30) +
            (exp_score * 0.12) +
            (sen_score * 0.08) +
            (edu_score * 0.05)
        )
        composite_score = round(float(np.clip(composite_score, 0.0, 100.0)), 1)

        # Tier assignment
        if composite_score >= 88.0:
            tier = "Exceptional Match"
            tier_class = "tier-exceptional"
            badge_icon = "🏆"
            verdict = "Top Candidate: Outstanding alignment across required skills, experience, and domain context."
        elif composite_score >= 74.0:
            tier = "Strong Match"
            tier_class = "tier-strong"
            badge_icon = "🌟"
            verdict = "High Potential: Strong skill overlap with minor addressable gaps."
        elif composite_score >= 55.0:
            tier = "Moderate Match"
            tier_class = "tier-moderate"
            badge_icon = "⚖️"
            verdict = "Fair Fit: Demonstrates core foundations, but requires bridging specific key skills."
        else:
            tier = "Low Match"
            tier_class = "tier-low"
            badge_icon = "⚠️"
            verdict = "Significant Gaps: Low keyword overlap and notable experience or technical discrepancies."

        # ATS Actionable Recommendations
        recommendations = cls.generate_recommendations(
            skill_res["missing_skills"], resume_data, job_data
        )

        return {
            "overall_score": composite_score,
            "tier": tier,
            "tier_class": tier_class,
            "badge_icon": badge_icon,
            "verdict": verdict,
            "category_scores": {
                "skills": {
                    "score": skill_score,
                    "weight": "45%",
                    "label": "Technical Skills Overlap"
                },
                "semantic": {
                    "score": semantic_score,
                    "weight": "30%",
                    "label": "Semantic & Contextual Similarity"
                },
                "experience": {
                    "score": exp_score,
                    "weight": "12%",
                    "label": "Experience Duration Fit",
                    "details": exp_res["status"]
                },
                "seniority": {
                    "score": sen_score,
                    "weight": "8%",
                    "label": "Seniority Level Alignment",
                    "details": sen_res["status"]
                },
                "education": {
                    "score": edu_score,
                    "weight": "5%",
                    "label": "Education Level Fit",
                    "details": edu_res["status"]
                }
            },
            "skills_analysis": skill_res,
            "experience_analysis": exp_res,
            "seniority_analysis": sen_res,
            "education_analysis": edu_res,
            "recommendations": recommendations,
            "candidate_summary": {
                "name": resume_data.get("candidate_name"),
                "email": resume_data.get("contact", {}).get("email"),
                "phone": resume_data.get("contact", {}).get("phone"),
                "experience_years": resume_data.get("experience_years"),
                "seniority": resume_data.get("seniority_level"),
                "education": resume_data.get("education_level"),
                "total_skills_count": len(resume_data.get("skills", [])),
                "word_count": resume_data.get("word_count")
            }
        }
