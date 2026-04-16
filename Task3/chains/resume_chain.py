
import re

def clean_extraction(resume_text):
    skills_match = re.search(r"Skills:\s*(.*)", resume_text)
    skills = skills_match.group(1).split(",") if skills_match else []

    tools_match = re.search(r"Tools:\s*(.*)", resume_text)
    tools = tools_match.group(1).split(",") if tools_match else []

    exp_match = re.search(r"(\d+)\s*years?", resume_text)
    experience = int(exp_match.group(1)) if exp_match else 0

    return {
        "skills": [s.strip() for s in skills],
        "experience": experience,
        "tools": [t.strip() for t in tools]
    }


def calculate_score(resume_data, jd_data):
    matched_skills = set(resume_data["skills"]) & set(jd_data["skills"])
    skill_score = (len(matched_skills) / len(jd_data["skills"])) * 70

    if resume_data["experience"] >= jd_data["experience"]:
        exp_score = 30
    else:
        exp_score = (resume_data["experience"] / jd_data["experience"]) * 30

    final_score = round(skill_score + exp_score, 2)

    return {
        "matched_skills": list(matched_skills),
        "skill_score": round(skill_score, 2),
        "experience_score": round(exp_score, 2),
        "final_score": final_score
    }
