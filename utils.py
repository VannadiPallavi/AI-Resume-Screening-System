def clean_text(text):
    """Remove extra spaces and new lines."""
    return " ".join(text.split())


def validate_resume_text(text):
    """Check whether the extracted resume text is usable."""
    if not text or len(text.strip()) < 30:
        return False

    return True