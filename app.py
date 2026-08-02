import streamlit as st
import PyPDF2

# Page Settings
st.set_page_config(page_title="AI Resume Screening System", page_icon="🤖")

# Title
st.title("🤖 AI Resume Screening System")
st.write("Welcome to my AI Resume Screening System!")
# Sidebar
st.sidebar.title("🤖 AI Resume Screening System")
st.sidebar.write("### Developed by")
st.sidebar.success("Vannadi Pallavi")

st.sidebar.markdown("---")

st.sidebar.write("### 📋 Features")
st.sidebar.write("✅ PDF Resume Upload")
st.sidebar.write("✅ Resume Score")
st.sidebar.write("✅ Skill Analysis")
st.sidebar.write("✅ Job Role Prediction")

st.sidebar.markdown("---")

st.sidebar.info("Upload your resume to get instant analysis.")

st.sidebar.markdown("---")

st.sidebar.write("### 📌 About Project")

st.sidebar.write(
    "An AI-powered Resume Screening System that analyzes resumes, "
    "checks skills, calculates resume score, and suggests suitable job roles."
)


# Upload PDF
uploaded_file = st.file_uploader("📄 Upload your Resume (PDF)", type="pdf")

if uploaded_file is not None:

    # Read PDF
    pdf_reader = PyPDF2.PdfReader(uploaded_file)

    text = ""
    for page in pdf_reader.pages:
        extracted = page.extract_text()
        if extracted:
            text += extracted

    # Show Resume
    st.subheader("📄 Resume Content")
    st.write(text)

    st.success("✅ Resume uploaded successfully!")

    # Skills List
    skills = [
        "Python",
        "Machine Learning",
        "Data Structures",
        "Streamlit",
        "Pandas",
        "NumPy"
    ]

    # Calculate Score
    score = 0

    for skill in skills:
        if skill.lower() in text.lower():
            score += 100 / len(skills)

    # Show Score
    st.subheader("📊 Resume Score")
    st.progress(int(score))
    st.write(f"Score: {int(score)}/100")

    # Feedback
    if score >= 80:
        st.success("🌟 Excellent Resume! You are job-ready.")
    elif score >= 60:
        st.info("👍 Good Resume! Add a few more skills to make it stronger.")
    else:
        st.warning("⚠️ Your resume needs improvement. Add more technical skills and projects.")

    # Required Skills
    required_skills = [
        "Python",
        "Machine Learning",
        "Data Structures",
        "Streamlit",
        "Pandas",
        "NumPy",
        "SQL",
        "Deep Learning"
    ]

    matched_skills = []
    missing_skills = []

    for skill in required_skills:
        if skill.lower() in text.lower():
            matched_skills.append(skill)
        else:
            missing_skills.append(skill)

                # Dashboard Metrics
    col1, col2, col3 = st.columns(3)

    col1.metric("📊 Resume Score", f"{int(score)}%")
    col2.metric("✅ Skills Matched", len(matched_skills))
    col3.metric("❌ Skills Missing", len(missing_skills))

    # Matched Skills
    st.markdown("### ✅ Matched Skills")
    for skill in matched_skills:
        st.write(f"✔️ {skill}")

    # Missing Skills
    st.markdown("### ❌ Missing Skills")
    for skill in missing_skills:
        st.write(f"❌ {skill}")

        # Resume Improvement Suggestions
    st.markdown("### 💡 Resume Improvement Suggestions")

    if len(missing_skills) == 0:
        st.success("🎉 Excellent! Your resume contains all the required skills.")
    else:
        st.write("You can improve your resume by learning or adding these skills:")
        for skill in missing_skills:
            st.write(f"➡️ Learn {skill}")
        

    # Job Role Prediction
    st.markdown("### 💼 Suggested Job Role")

    if "machine learning" in text.lower() and "python" in text.lower():
        st.success("🤖 AI / Machine Learning Engineer")

    elif "python" in text.lower():
        st.success("🐍 Python Developer")

    elif "data structures" in text.lower():
        st.success("💻 Software Developer")

    elif "sql" in text.lower():
        st.success("📊 Data Analyst")

    else:
        st.info("🎯 General IT Fresher")

     # Download Report
    st.markdown("### 📥 Download Resume Report")

    report = f"""
AI Resume Screening Report

Candidate Resume Analysis

Resume Score: {int(score)}/100

Matched Skills:
{', '.join(matched_skills)}

Missing Skills:
{', '.join(missing_skills)}

Suggested Job Role:
AI / Machine Learning Engineer

"""

    st.download_button(
        label="📄 Download Report",
        data=report,
        file_name="Resume_Analysis_Report.txt",
        mime="text/plain"
    ) 
