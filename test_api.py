"""Quick integration test script for MatchPulse APIs."""
import urllib.request
import json
import uuid
from backend.samples import SAMPLE_JOBS, SAMPLE_RESUMES

def test_batch_aiml():
    boundary = "----WebKitFormBoundary" + uuid.uuid4().hex
    lines = []

    # AI / ML Job
    lines.extend([
        f"--{boundary}",
        'Content-Disposition: form-data; name="job_text"',
        "",
        SAMPLE_JOBS[1]["text"],
        f"--{boundary}",
        'Content-Disposition: form-data; name="job_title"',
        "",
        SAMPLE_JOBS[1]["title"]
    ])

    # resume_files
    for r in SAMPLE_RESUMES:
        clean_name = r["name"].replace(" ", "_")
        lines.extend([
            f"--{boundary}",
            f'Content-Disposition: form-data; name="resume_files"; filename="{clean_name}.txt"',
            "Content-Type: text/plain",
            "",
            r["text"]
        ])

    lines.append(f"--{boundary}--")
    body = "\r\n".join(lines).encode("utf-8")

    req = urllib.request.Request("http://127.0.0.1:8000/api/batch-match", data=body, method="POST")
    req.add_header("Content-Type", f"multipart/form-data; boundary={boundary}")

    with urllib.request.urlopen(req) as resp:
        res = json.loads(resp.read().decode("utf-8"))
        print("\n--- AI / ML Job Leaderboard ---")
        print("Total applicants ranked:", res["total_applicants"])
        for idx, c in enumerate(res["leaderboard"]):
            print(f"Rank {idx+1}: {c['candidate_name']} ({c['filename']}) - Score: {c['overall_score']}% - Tier: {c['tier']}")

if __name__ == "__main__":
    test_batch_aiml()
