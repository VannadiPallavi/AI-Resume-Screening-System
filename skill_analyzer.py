SKILLS = [
    "python",
    "c++",
    "java",
    "sql",
    "machine learning",
    "deep learning",
    "artificial intelligence",
    "numpy",
    "pandas",
    "scikit-learn",
    "tensorflow",
    "pytorch",
    "streamlit",
    "html",
    "css",
    "javascript",
    "git",
    "github",
    "data structures",
    "algorithms",
    "excel",
    "power bi",
    "nlp",
    "computer vision",
    "statistics",
    "oop",
    "rest api",
    "flask",
    "django"
]


def analyze_skills(text):
    lower_text = text.lower()

    matched_skills = [
        skill for skill in SKILLS
        if skill in lower_text
    ]

    missing_skills = [
        skill for skill in SKILLS
        if skill not in lower_text
    ]

    return {
        "matched_skills": matched_skills,
        "missing_skills": missing_skills
    }