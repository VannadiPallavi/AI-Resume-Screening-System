import streamlit as st

from resume_parser import extract_text_from_pdf
from skill_analyzer import analyze_skills
from resume_scorer import calculate_score
from job_role_predictor import predict_job_role
from report_generator import generate_report


st.set_page_config(
    page_title="AI Resume Screening System",
    page_icon="📄",
    layout="wide"
)


st.title("📄 AI-Powered Resume Screening and Job Role Recommendation System")

st.write(
    "Upload a PDF resume to analyze skills, calculate a resume score, "
    "and recommend a suitable job role."
)


uploaded_file = st.file_uploader(
    "Upload your Resume (PDF only)",
    type=["pdf"]
)


if uploaded_file:

    try:
        # Step 1: Extract resume text
        text = extract_text_from_pdf(uploaded_file)

        if not text.strip():
            st.error("No readable text was found in the PDF.")
            st.stop()

        # Step 2: Analyze skills
        analysis = analyze_skills(text)

        # Step 3: Calculate score
        score = calculate_score(
            text,
            analysis["matched_skills"]
        )

        # Step 4: Predict job role using ML
        role, similarity = predict_job_role(text)

        # Dashboard
        st.subheader("📊 Resume Analysis")

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Resume Score",
            f"{score}/100"
        )

        col2.metric(
            "Matched Skills",
            len(analysis["matched_skills"])
        )

        col3.metric(
            "Recommended Role",
            role
        )

        # Extracted text
        st.subheader("1. Extracted Resume Text")

        with st.expander("View Extracted Text"):
            st.text(text[:10000])

        # Skill analysis
        st.subheader("2. Skill Analysis")

        left, right = st.columns(2)

        with left:
            st.write("### ✅ Matched Skills")

            if analysis["matched_skills"]:
                for skill in analysis["matched_skills"]:
                    st.success(skill)
            else:
                st.write("No matching skills detected.")

        with right:
            st.write("### ⚠️ Missing Skills")

            for skill in analysis["missing_skills"][:10]:
                st.warning(skill)

        # Job recommendation
        st.subheader("3. Job Role Recommendation")

        st.info(
            f"Recommended Role: **{role}**"
        )

        st.write(
            f"TF-IDF Cosine Similarity: **{similarity:.2f}**"
        )

        # Suggestions
        st.subheader("4. Resume Improvement Suggestions")

        suggestions = []

        if len(analysis["matched_skills"]) < 5:
            suggestions.append(
                "Add more relevant technical skills."
            )

        if "education" not in text.lower():
            suggestions.append(
                "Add a clear Education section."
            )

        if "project" not in text.lower():
            suggestions.append(
                "Add relevant academic or personal projects."
            )

        if (
            "experience" not in text.lower()
            and "internship" not in text.lower()
        ):
            suggestions.append(
                "Add internship or practical experience when applicable."
            )

        if not suggestions:
            suggestions.append(
                "The resume contains the main sections and skills detected by the system."
            )

        for suggestion in suggestions:
            st.write("•", suggestion)

        # Report
        st.subheader("5. Download Report")

        report = generate_report(
            text,
            score,
            analysis,
            role,
            similarity,
            suggestions
        )

        st.download_button(
            label="⬇️ Download Analysis Report",
            data=report,
            file_name="resume_analysis_report.txt",
            mime="text/plain"
        )

        st.success("Resume analysis completed successfully!")

        st.caption("Developed by Vannadi Pallavi")

    except Exception as error:

        st.error(
            f"Unable to process the resume: {error}"
        )