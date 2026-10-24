# ⚡ MatchPulse: AI-Powered Resume–Job Matching & ATS Optimization System

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10%2B-f00010?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.110%2B-0d0103?style=for-the-badge&logo=fastapi&logoColor=f00010)
![NumPy](https://img.shields.io/badge/NumPy-LSA%20SVD-a00010?style=for-the-badge&logo=numpy&logoColor=white)
![UI](https://img.shields.io/badge/UI-Tactical%20Crimson-f00010?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-white?style=for-the-badge&color=0d0103)

**An enterprise-grade, hybrid NLP & latent semantic matching engine designed to evaluate, score, and rank candidate resumes against target job descriptions with millisecond speed and zero external API dependencies.**

[Key Features](#-key-features) • [Architecture](#-architecture) • [Algorithm](#-hybrid-matching-algorithm) • [Quickstart](#-quickstart-guide) • [REST API](#-rest-api-documentation) • [Benchmarks](#-benchmark-results)

</div>

---

## 🌟 Key Features

### 1. 🎛️ Dual-Pane Tactical Match Studio
- **Multi-Format Document Ingestion**: Ingests resumes in **PDF** (`.pdf`), **Word** (`.docx`), and plain text (`.txt`), or paste formatted text directly.
- **Job Specification Parser**: Automatically extracts role titles, required skills, duration requirements, and seniority criteria from raw job listings.
- **Instant Quick Presets**: Test candidate-job combinations with 1 click:
  - **Senior Full-Stack**: Alex Morgan vs. CloudScale Technologies
  - **AI / ML Specialist**: Elena Rostova vs. DeepCognition AI
  - **Junior Profile Gap Demo**: Marcus Vance vs. Senior Full-Stack Role

### 2. 📊 Granular Match Analytics Dashboard
- **Animated SVG Radial Gauge**: Real-time composite match score (0 - 100%) with radiant crimson glows and color-calibrated tiers:
  - 🏆 **Exceptional Match** (88% – 100%)
  - 🌟 **Strong Match** (74% – 87%)
  - ⚖️ **Moderate Match** (55% – 73%)
  - ⚠️ **Low Match / Significant Gaps** (< 55%)
- **5-Dimensional Fit Telemetry**:
  - **Technical Skills Overlap (45% weight)**: Exact and synonym-matched skill taxonomy mapping across 1,200+ skills.
  - **Semantic Context Alignment (30% weight)**: Sublinear TF-IDF + Latent Semantic Analysis (LSA) dense concept projection.
  - **Experience Duration Fit (12% weight)**: Candidate years vs. required years.
  - **Seniority Level Alignment (8% weight)**: Role seniority ladder hierarchy (Junior ➔ Lead ➔ Architect).
  - **Education Level Fit (5% weight)**: Degree alignment (BSc, MSc, PhD, etc.).
- **Interactive Skills Matrix**: Granular pill tags categorized into **Matched**, **Missing Critical Gaps**, and **Bonus Candidate Skills**.
- **Technical Domain Fulfillment**: Visual progress meters across Frontend, Backend, Cloud & DevOps, AI/Data Science, and Databases.

### 3. 🎯 ATS Resume Optimizer & Tailoring Studio
- **ATS Formatting & Health Checklist**: Automated checks for standard section headings, word count density, and direct contact details.
- **Tailored Accomplishment Bullet Points**: Automatically generates bullet points with click-to-copy functionality targeting missing keywords.
- **Actionable ATS Recommendations**: Sorted by High, Medium, and Low impact to maximize recruiter scan rates.

### 4. 👥 Batch Applicant Ranker (Multi-Resume Cohort Mode)
- **Cohort Upload**: Process and evaluate multiple candidate resumes simultaneously against a single target job description.
- **Candidate Leaderboard**: Sorted table displaying rank (🥇 Gold, 🥈 Silver, 🥉 Bronze), composite fit score, tier, experience, matched skills, and key missing skills.
- **CSV Export**: One-click download of the complete ranked cohort table for recruitment pipelines.

### 5. 🔍 Skills & Domain Taxonomy Explorer
- Over **1,200+** indexed technical and soft skills across 8 core industry domains.
- Live fuzzy search modal for exploring skill aliases and categories.

---

## 🎨 Design Philosophy: Tactical Crimson & Obsidian

MatchPulse is styled with a high-intensity, dark-mode tactical theme:
- **Obsidian Black (`#000000`)** base with deep volcanic panels (`#0d0103`).
- **Electric Blood Crimson (`#f00010`)** accents and radiant glows.
- **Halftone Dot Matrix & Cyber Grid** overlay with masked vignette.
- **Ambient Volcanic Red Smoke & Floating Embers** drifting across the viewport.
- **High-contrast typography**: `Oswald` (bold condensed uppercase display), `IBM Plex Mono` (tactical data & telemetry), and `Inter` (crisp body text).

---

## 🧠 Hybrid Matching Algorithm

MatchPulse uses a balanced, multi-tier evaluation algorithm designed to eliminate keyword stuffing while rewarding contextual relevance:

$$
\text{Overall Score} = (S_{\text{skills}} \times 0.45) + (S_{\text{semantic}} \times 0.30) + (S_{\text{exp}} \times 0.12) + (S_{\text{sen}} \times 0.08) + (S_{\text{edu}} \times 0.05)
$$

### 1. Sublinear TF-IDF + Latent Semantic Analysis (LSA)
- **Sublinear TF Scaling**: Uses $1 + \log(\text{TF})$ for $\text{TF} > 0$ to prevent repetitive keyword saturation from inflating scores.
- **Dense SVD Concept Projection**: Uses Singular Value Decomposition ($\mathbf{X} = \mathbf{U} \mathbf{\Sigma} \mathbf{V}^T$) to compute latent topical vectors, enabling conceptual similarity detection even when exact wordings differ.

### 2. Ontology-Driven Skill Taxonomy
- Standardizes aliases:
  - `k8s` ➔ `Kubernetes`
  - `react.js` / `reactjs` ➔ `React`
  - `postgres` ➔ `PostgreSQL`
  - `aws ec2` / `aws lambda` ➔ `AWS`
- Groups skills across 8 domains (Frontend, Backend, Cloud/DevOps, Databases, AI/ML, Testing, Methodologies, Soft Skills).

---

## 🏗️ Architecture

```
MatchPulse/
├── backend/
│   ├── __init__.py
│   ├── taxonomy.py      # 1,200+ skill taxonomy, synonym mapping, seniority & degree rankings
│   ├── parser.py        # Multi-format parser (PDF, DOCX, TXT), section segmenter & metadata
│   ├── engine.py        # Hybrid Matcher (TF-IDF + LSA SVD dense vectors, gap matrix & ATS suggestions)
│   ├── samples.py       # Pre-loaded realistic sample resumes and job listings
│   └── main.py          # FastAPI application serving REST endpoints and the UI
├── frontend/
│   ├── index.html       # Modern SPA structure with tabbed navigation & glassmorphism
│   ├── style.css        # Vanilla CSS Design System with dark mode, animations & responsive grid
│   └── app.js           # Reactive UI engine with radial progress animations & batch processor
├── run.py               # Single-command server launcher with automatic port detection
├── requirements.txt     # Python dependencies
├── test_api.py          # Integration test suite validating batch ranking
└── README.md            # System documentation
```

---

## ⚡ Quickstart Guide

### 1. Clone the Repository
```bash
git clone https://github.com/mraffankhan/MatchPulse.git
cd MatchPulse
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Application
```bash
python run.py
```

The system will start and automatically open your default browser:
- **Web Dashboard**: [http://127.0.0.1:8000](http://127.0.0.1:8000)
- **Interactive Swagger API Docs**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 📡 REST API Documentation

### `POST /api/match`
Execute a hybrid match between a resume (file or text) and a job description.

**Form Parameters:**
- `resume_file` *(optional)*: Uploaded PDF, DOCX, or TXT file.
- `resume_text` *(optional)*: Raw pasted resume text.
- `job_file` *(optional)*: Uploaded PDF, DOCX, or TXT file.
- `job_text` *(optional)*: Raw pasted job description.
- `job_title` *(optional)*: Target role title.

**Sample Response:**
```json
{
  "match": {
    "overall_score": 81.4,
    "tier": "Strong Match",
    "tier_class": "tier-strong",
    "badge_icon": "🌟",
    "category_scores": {
      "skills": { "score": 84.4, "weight": "45%" },
      "semantic": { "score": 61.5, "weight": "30%" },
      "experience": { "score": 100.0, "weight": "12%" },
      "seniority": { "score": 100.0, "weight": "8%" },
      "education": { "score": 100.0, "weight": "5%" }
    },
    "skills_analysis": {
      "matched_count": 27,
      "total_required": 32,
      "matched_skills": [ ... ],
      "missing_skills": [ ... ]
    }
  }
}
```

### `POST /api/batch-match`
Evaluate and rank multiple resumes against a target job description in a single call.

**Form Parameters:**
- `job_text`: Required job description string.
- `job_title`: Title of the role.
- `resume_files`: Array of uploaded resume files.

---

## 🧪 Benchmark Results

Using the built-in [test_api.py](file:///d:/Resume%E2%80%93Job%20Matching%20System/test_api.py) benchmark suite:

### Test Case A: Senior Full-Stack Engineer Role
| Rank | Candidate | Fit Score | Tier | Profile Summary |
| :---: | :--- | :---: | :---: | :--- |
| 🥇 **1** | **Alex Morgan** | **81.4%** | 🌟 Strong Match | 6 yrs exp, React, TypeScript, FastAPI, AWS, Docker |
| 🥈 **2** | **Elena Rostova** | **38.0%** | ⚠️ Low Match | ML specialist (Python, PyTorch) missing frontend stack |
| 🥉 **3** | **Marcus Vance** | **23.9%** | ⚠️ Low Match | Junior web dev (1.5 yrs exp) missing architecture depth |

### Test Case B: AI / Machine Learning Engineer Role
| Rank | Candidate | Fit Score | Tier | Profile Summary |
| :---: | :--- | :---: | :---: | :--- |
| 🥇 **1** | **Elena Rostova** | **85.8%** | 🌟 Strong Match | 4 yrs exp, PyTorch, Transformers, RAG, LangChain |
| 🥈 **2** | **Alex Morgan** | **37.9%** | ⚠️ Low Match | Full-stack developer with minimal deep learning overlap |
| 🥉 **3** | **Marcus Vance** | **20.5%** | ⚠️ Low Match | Junior web developer |

---

## 📄 License

Distributed under the **MIT License**. See `LICENSE` for more information.

---

## 👤 Author

**Affan Khan**
- GitHub: [@mraffankhan](https://github.com/mraffankhan)
- Project: [MatchPulse](https://github.com/mraffankhan/MatchPulse)
