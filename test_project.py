from skill_analyzer import analyze_skills
from resume_scorer import calculate_score
from job_role_predictor import predict_job_role
from utils import clean_text, validate_resume_text


def test_skill_analysis():
    result = analyze_skills(
        "Python, Pandas, Machine Learning and SQL"
    )

    assert "python" in result["matched_skills"]
    assert "sql" in result["matched_skills"]


def test_score():
    score = calculate_score(
        "education skills project experience contact",
        ["python", "pandas"]
    )

    assert 0 <= score <= 100


def test_prediction():
    role, similarity = predict_job_role(
        "Python machine learning pandas numpy artificial intelligence"
    )

    assert isinstance(role, str)
    assert 0 <= similarity <= 1


def test_utils():
    assert clean_text("hello   world") == "hello world"
    assert validate_resume_text(
        "This is a sample resume with enough readable text."
    ) is True
    assert validate_resume_text("") is False


if __name__ == "__main__":
    test_skill_analysis()
    test_score()
    test_prediction()
    test_utils()

    print("All tests passed successfully.")