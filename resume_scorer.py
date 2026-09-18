def calculate_score(text, matched_skills):
    lower_text = text.lower()

    # Maximum 50 marks for technical skills
    skill_score = min(len(matched_skills) * 5, 50)

    # 10 marks for each important resume section
    sections = [
        "education",
        "project",
        "experience",
        "skills",
        "contact"
    ]

    section_score = 0

    for section in sections:
        if section in lower_text:
            section_score += 10

    total_score = skill_score + section_score

    return min(total_score, 100)