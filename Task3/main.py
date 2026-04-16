
from chains.resume_chain import clean_extraction, calculate_score

# Job Description
job_description = """
We are hiring a Data Scientist with Python, ML, DL, SQL skills.
Minimum 2 years experience required.
"""

# Resume
resume = """
John Doe
Skills: Python, Machine Learning, Deep Learning, SQL
Experience: 3 years
Tools: Python, SQL
"""

# JD Data (manually structured)
jd_data = {
    "skills": ["Python", "Machine Learning", "Deep Learning", "SQL"],
    "experience": 2
}

# Process
resume_data = clean_extraction(resume)
result = calculate_score(resume_data, jd_data)

print("Resume Data:", resume_data)
print("Score:", result)
