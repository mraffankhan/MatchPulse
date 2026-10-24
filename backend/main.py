"""
FastAPI Application Entry Point for Resume-Job Matching System.
Provides RESTful APIs for parsing, single matching, batch candidate ranking, and static web serving.
"""

import os
from typing import List, Optional
from fastapi import FastAPI, File, UploadFile, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse
from pydantic import BaseModel

from .parser import ResumeParser
from .engine import HybridMatcher
from .samples import SAMPLE_JOBS, SAMPLE_RESUMES
from .taxonomy import SKILL_TAXONOMY

app = FastAPI(
    title="Resume–Job Matching System API",
    description="High-performance hybrid NLP and skill taxonomy matching system.",
    version="1.0.0"
)

# Enable CORS for local development and integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

FRONTEND_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "frontend"))


# Request Models
class TextMatchRequest(BaseModel):
    resume_text: str
    job_text: str
    job_title: Optional[str] = "Target Job Description"
    resume_name: Optional[str] = "Candidate Resume"


class BatchCandidateItem(BaseModel):
    name: str
    text: str


class BatchMatchRequest(BaseModel):
    job_text: str
    job_title: Optional[str] = "Target Role"
    candidates: List[BatchCandidateItem]


@app.get("/api/health")
def health_check():
    return {"status": "ok", "service": "Resume-Job Matching System", "version": "1.0.0"}


@app.get("/api/samples")
def get_sample_data():
    """Retrieve pre-configured sample jobs and candidate resumes."""
    return {
        "jobs": SAMPLE_JOBS,
        "resumes": SAMPLE_RESUMES
    }


@app.get("/api/skills-taxonomy")
def get_taxonomy():
    """Retrieve the system's categorized skill taxonomy."""
    return SKILL_TAXONOMY


@app.post("/api/parse-resume")
async def parse_resume_endpoint(
    file: Optional[UploadFile] = File(None),
    text: Optional[str] = Form(None)
):
    """Parse a single resume from file upload or raw text."""
    if file:
        content = await file.read()
        try:
            raw_text = ResumeParser.parse_document(file.filename, content)
        except Exception as e:
            raise HTTPException(status_code=400, detail=f"Error reading file: {str(e)}")
        filename = file.filename
    elif text:
        raw_text = text.strip()
        filename = "pasted_resume.txt"
    else:
        raise HTTPException(status_code=400, detail="Must provide either a file or text.")

    if not raw_text.strip():
        raise HTTPException(status_code=400, detail="Document appears to be empty or unreadable.")

    analysis = ResumeParser.analyze_resume(raw_text, filename=filename)
    return analysis


@app.post("/api/match")
async def match_endpoint(
    resume_file: Optional[UploadFile] = File(None),
    resume_text: Optional[str] = Form(None),
    job_file: Optional[UploadFile] = File(None),
    job_text: Optional[str] = Form(None),
    job_title: Optional[str] = Form("Target Job")
):
    """
    Execute hybrid match between resume and job description.
    Supports file uploads (PDF/DOCX/TXT) or pasted raw text.
    """
    # 1. Resolve Resume Text
    if resume_file:
        content = await resume_file.read()
        try:
            r_text = ResumeParser.parse_document(resume_file.filename, content)
            r_fname = resume_file.filename
        except Exception as e:
            raise HTTPException(status_code=400, detail=f"Error reading resume file: {str(e)}")
    elif resume_text:
        r_text = resume_text.strip()
        r_fname = "pasted_resume.txt"
    else:
        raise HTTPException(status_code=400, detail="Resume file or text is required.")

    # 2. Resolve Job Text
    if job_file:
        content = await job_file.read()
        try:
            j_text = ResumeParser.parse_document(job_file.filename, content)
            j_title = job_file.filename
        except Exception as e:
            raise HTTPException(status_code=400, detail=f"Error reading job description file: {str(e)}")
    elif job_text:
        j_text = job_text.strip()
        j_title = job_title or "Target Job"
    else:
        raise HTTPException(status_code=400, detail="Job description file or text is required.")

    if not r_text:
        raise HTTPException(status_code=400, detail="Resume content is empty.")
    if not j_text:
        raise HTTPException(status_code=400, detail="Job description content is empty.")

    # 3. Parse Both Documents
    resume_data = ResumeParser.analyze_resume(r_text, filename=r_fname)
    job_data = ResumeParser.analyze_job(j_text, title=j_title)

    # 4. Compute Hybrid Match
    match_result = HybridMatcher.match(resume_data, job_data)

    return {
        "match": match_result,
        "resume": {
            "filename": resume_data["filename"],
            "candidate_name": resume_data["candidate_name"],
            "skills": resume_data["skills"],
            "experience_years": resume_data["experience_years"],
            "seniority_level": resume_data["seniority_level"],
            "education_level": resume_data["education_level"],
            "sections": resume_data["sections"],
            "contact": resume_data["contact"]
        },
        "job": {
            "title": job_data["title"],
            "skills": job_data["skills"],
            "required_years": job_data["required_years"],
            "required_seniority": job_data["required_seniority"],
            "required_education": job_data["required_education"]
        }
    }


@app.post("/api/batch-match")
async def batch_match_endpoint(
    job_text: str = Form(...),
    job_title: Optional[str] = Form("Target Role"),
    resume_files: List[UploadFile] = File(...)
):
    """
    Rank multiple candidate resume uploads against a single Job Description.
    """
    if not resume_files:
        raise HTTPException(status_code=400, detail="At least one resume file must be uploaded.")

    job_data = ResumeParser.analyze_job(job_text, title=job_title or "Target Role")
    results = []

    for file in resume_files:
        try:
            content = await file.read()
            text = ResumeParser.parse_document(file.filename, content)
            if not text.strip():
                continue
            r_data = ResumeParser.analyze_resume(text, filename=file.filename)
            match_res = HybridMatcher.match(r_data, job_data)

            results.append({
                "filename": file.filename,
                "candidate_name": r_data["candidate_name"],
                "overall_score": match_res["overall_score"],
                "tier": match_res["tier"],
                "tier_class": match_res["tier_class"],
                "badge_icon": match_res["badge_icon"],
                "experience_years": r_data["experience_years"],
                "seniority": r_data["seniority_level"],
                "education": r_data["education_level"],
                "matched_skills_count": len(match_res["skills_analysis"]["matched_skills"]),
                "missing_skills_count": len(match_res["skills_analysis"]["missing_skills"]),
                "matched_skills": [s["name"] for s in match_res["skills_analysis"]["matched_skills"]],
                "missing_skills": [s["name"] for s in match_res["skills_analysis"]["missing_skills"][:5]],
                "email": r_data["contact"].get("email"),
                "phone": r_data["contact"].get("phone"),
                "verdict": match_res["verdict"]
            })
        except Exception as e:
            results.append({
                "filename": file.filename,
                "error": f"Failed to parse: {str(e)}",
                "overall_score": 0.0
            })

    # Sort descending by match score
    results.sort(key=lambda x: x.get("overall_score", 0), reverse=True)

    return {
        "job": {
            "title": job_data["title"],
            "required_skills_count": len(job_data["skills"]),
            "required_years": job_data["required_years"]
        },
        "total_applicants": len(results),
        "leaderboard": results
    }


# Mount Frontend Static Assets
if os.path.exists(FRONTEND_DIR):
    app.mount("/static", StaticFiles(directory=FRONTEND_DIR), name="static")


@app.get("/")
def serve_index():
    index_path = os.path.join(FRONTEND_DIR, "index.html")
    if os.path.exists(index_path):
        return FileResponse(index_path)
    return {"message": "Resume Matching Backend running. Frontend index.html not yet found."}
