# AI Resume Screening System

## Overview

The AI Resume Screening System is an intelligent recruitment solution developed using Python, Streamlit, Natural Language Processing (NLP), and BERT-based semantic matching. The system automates the process of screening resumes by comparing candidate profiles with job descriptions and generating matching scores, rankings, and recruiter insights.

This project helps recruiters reduce manual effort, improve hiring efficiency, and identify the most suitable candidates based on skills and job requirements.

---

## Problem Statement

Recruiters often receive hundreds of resumes for a single job opening. Manually reviewing each resume is time-consuming and prone to human bias. Organizations need an automated system that can efficiently analyze resumes, compare them with job descriptions, and rank candidates based on relevance.

---

## Objectives

* Automate resume screening and candidate evaluation.
* Extract relevant skills from resumes and job descriptions.
* Calculate candidate-job matching scores.
* Rank candidates based on their suitability.
* Provide visual analytics for recruiters.
* Generate downloadable reports for hiring decisions.

---

## Features

* Resume Upload (PDF)
* Job Description Analysis
* Resume Text Extraction
* Skill Extraction using NLP
* BERT-Based Semantic Matching
* ATS Score Calculation
* Candidate Ranking
* Recruiter Analytics Dashboard
* Interactive Charts and Visualizations
* Excel Report Download
* SQLite Database Integration
* Modern User Interface using Streamlit

---

## System Architecture

User Uploads Resume and Job Description

↓

Resume Parser

↓

Skill Extraction Module

↓

BERT Matching Engine

↓

ATS Score Calculation

↓

Candidate Ranking

↓

Database Storage

↓

Recruiter Dashboard & Reports

---

## Technology Stack

### Frontend

* Streamlit
* HTML
* CSS
* Plotly

### Backend

* Python
* Pandas
* SQLite

### AI / NLP

* Sentence Transformers
* BERT
* Scikit-Learn

### Database

* SQLite

### Visualization

* Plotly Express

---

## Installation

### Clone Repository

```bash
git clone https://github.com/your-username/AI-Resume-Screening-System.git
cd AI-Resume-Screening-System
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / Mac

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Required Libraries

```bash
pip install streamlit
pip install pandas
pip install plotly
pip install pdfplumber
pip install sentence-transformers
pip install scikit-learn
pip install openpyxl
```

---

## Running the Application

```bash
streamlit run app.py
```

The application will start locally at:

```text
http://localhost:8501
```

---

## Workflow

1. Upload one or more PDF resumes.
2. Enter the job description.
3. Click the Analyze Resume button.
4. The system extracts resume content.
5. Skills are identified using NLP techniques.
6. BERT calculates semantic similarity between resume and job description.
7. ATS scores are generated.
8. Candidates are ranked automatically.
9. Results are stored in the database.
10. Recruiters can view analytics and download reports.

---

## Dashboard Features

* Total Candidates
* Average Matching Score
* Top Candidate Identification
* Candidate Ranking Table
* Score Distribution Chart
* Recommendation Distribution Chart
* Downloadable Excel Reports

---

## Future Enhancements

* Multi-language Resume Support
* Resume Summarization using Generative AI
* Cloud Deployment using AWS
* Email Notifications
* Interview Recommendation Engine
* Applicant Tracking System Integration
* Advanced Skill Gap Analysis

---

## Results

The system successfully automates resume screening by extracting skills, calculating candidate-job matching scores, ranking applicants, and presenting recruiter-friendly analytics through an interactive dashboard.

---

## Conclusion

The AI Resume Screening System demonstrates how Artificial Intelligence and Natural Language Processing can streamline recruitment processes. By automating resume evaluation and candidate ranking, the system helps organizations make faster and more informed hiring decisions while reducing manual effort.

---

## Author

Harika Lankalapalli

B.Tech Computer Science and Engineering

KL University

---

## License

This project is developed for educational and learning purposes.
