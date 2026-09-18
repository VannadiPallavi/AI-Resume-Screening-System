# AI-Powered Resume Screening and Job Role Recommendation System

## 1. Project Overview

The AI-Powered Resume Screening and Job Role Recommendation System is a Python-based application that analyzes resumes automatically.

The system accepts a resume in PDF format, extracts the resume text, identifies technical skills, calculates a resume score, and recommends a suitable job role using Machine Learning techniques.

## 2. Problem Statement

Manual resume screening can take significant time when resumes need to be reviewed for relevant skills and suitable job roles.

This project provides an automated approach for analyzing a resume and helping users understand their skills, missing skills, resume score, and suitable job role.

## 3. Objectives

- Extract text from PDF resumes.
- Identify technical skills present in a resume.
- Detect missing skills.
- Calculate a resume score.
- Recommend a suitable job role using Machine Learning.
- Provide resume improvement suggestions.
- Generate a downloadable analysis report.

## 4. Features

- PDF Resume Upload
- Resume Text Extraction
- Technical Skill Analysis
- Matched Skill Detection
- Missing Skill Detection
- Resume Score Calculation
- Job Role Recommendation
- TF-IDF and Cosine Similarity
- Resume Improvement Suggestions
- Downloadable Analysis Report

## 5. Technologies Used

- Python
- Streamlit
- PyPDF2
- Scikit-learn
- TF-IDF
- Cosine Similarity
- Git and GitHub

## 6. System Workflow

1. User uploads a PDF resume.
2. The system extracts text from the PDF.
3. The extracted text is analyzed for technical skills.
4. Matched and missing skills are identified.
5. A resume score is calculated.
6. The resume is compared with job-role descriptions using TF-IDF.
7. Cosine Similarity is used to recommend a suitable job role.
8. Improvement suggestions are displayed.
9. The user can download the analysis report.

## 7. Project Structure

```text
AI-Resume-Screening-System/
│
├── app.py
├── resume_parser.py
├── skill_analyzer.py
├── resume_scorer.py
├── job_role_predictor.py
├── report_generator.py
├── utils.py
├── test_project.py
├── requirements.txt
├── README.md
├── statement.md
│
└── data/
    └── skills_roles.csv