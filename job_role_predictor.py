import csv
from pathlib import Path

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


DATA_PATH = Path(__file__).parent / "data" / "skills_roles.csv"


def load_roles():
    roles = []

    with open(DATA_PATH, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            roles.append(row)

    return roles


def predict_job_role(resume_text):
    roles = load_roles()

    role_texts = [role["skills"] for role in roles]

    vectorizer = TfidfVectorizer(stop_words="english")

    matrix = vectorizer.fit_transform(
        role_texts + [resume_text]
    )

    similarities = cosine_similarity(
        matrix[-1],
        matrix[:-1]
    ).flatten()

    best_index = similarities.argmax()

    recommended_role = roles[best_index]["role"]
    similarity_score = float(similarities[best_index])

    return recommended_role, similarity_score