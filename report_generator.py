def generate_report(text, score, analysis, role, similarity, suggestions):

    report = [
        "AI-POWERED RESUME SCREENING AND JOB ROLE RECOMMENDATION SYSTEM",
        "=" * 60,
        "",
        f"Resume Score: {score}/100",
        f"Recommended Job Role: {role}",
        f"Role Similarity Score: {similarity:.2f}",
        "",
        "MATCHED SKILLS",
        "-" * 20
    ]

    for skill in analysis["matched_skills"]:
        report.append(f"- {skill}")

    report.extend([
        "",
        "MISSING SKILLS",
        "-" * 20
    ])

    for skill in analysis["missing_skills"]:
        report.append(f"- {skill}")

    report.extend([
        "",
        "IMPROVEMENT SUGGESTIONS",
        "-" * 30
    ])

    for suggestion in suggestions:
        report.append(f"- {suggestion}")

    return "\n".join(report).encode("utf-8")