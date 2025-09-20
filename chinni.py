import re

def parse_resume(text):
    # Extract email
    email = re.findall(r'\S+@\S+', text)
    email = email[0] if email else None

    # Extract phone number (simple pattern for 10-15 digits including + and -)
    phone = re.findall(r'(\+?\d[\d -]{8,}\d)', text)
    phone = phone[0] if phone else None

    # Extract name - assume the first line is the name (simple heuristic)
    lines = text.strip().split('\n')
    name = lines[0] if lines else None

    # Extract skills - look for a "Skills" section and grab comma-separated values
    skills = []
    skills_section = re.search(r'Skills[:\-]?\s*(.*)', text, re.IGNORECASE)
    if skills_section:
        skills_text = skills_section.group(1)
        # split by comma or semicolon
        skills = [skill.strip() for skill in re.split(r'[;,]', skills_text)]

    return {
        'Name': name,
        'Email': email,
        'Phone': phone,
        'Skills': skills
    }

# Example usage
resume_text = """
John Doe
john.doe@example.com
+1 234-567-8900

Professional Summary
Experienced software engineer with a focus on Python and data analysis.

Skills: Python, Data Analysis, Machine Learning, SQL, Git
"""

parsed = parse_resume(resume_text)
print(parsed)
