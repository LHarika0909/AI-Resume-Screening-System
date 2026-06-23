import streamlit as st
st.set_page_config(page_title="AI Resume Screening System", layout="wide")
st.title("AI Resume Screening System")
st.info("Project template generated. Complete and customize as needed.")
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="AI Resume Screening System",
    layout="wide"
)
st.markdown("""
<style>

/* Background */
.stApp {
    background: #F4F7FE;
}

/* Main Container */
.main .block-container {
    padding-top: 2rem;
    padding-left: 3rem;
    padding-right: 3rem;
}

/* Headings */
h1 {
    color: #1E293B !important;
    font-weight: 700;
}

h2, h3 {
    color: #1E293B !important;
}

/* Labels */
label {
    color: #1E293B !important;
    font-weight: 600 !important;
}

/* Upload Box */
[data-testid="stFileUploader"] {
    background: white;
    border-radius: 15px;
    padding: 20px;
    border: 2px dashed #6366F1;
    box-shadow: 0 4px 15px rgba(0,0,0,0.08);
}

/* Text Area */
textarea {
    border-radius: 12px !important;
    border: 2px solid #6366F1 !important;
    background: white !important;
    color: black !important;
}

/* Buttons */
.stButton > button {
    background: linear-gradient(90deg,#6366F1,#8B5CF6);
    color: white;
    border: none;
    border-radius: 12px;
    height: 50px;
    width: 220px;
    font-weight: bold;
    font-size: 17px;
}

/* DataFrame */
[data-testid="stDataFrame"] {
    background: white;
    border-radius: 15px;
    padding: 10px;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: linear-gradient(
        180deg,
        #0F172A,
        #1E3A8A
    );
}

section[data-testid="stSidebar"] * {
    color: white !important;
}

</style>
""", unsafe_allow_html=True)

from utils.parser import extract_text
from utils.extractor import extract_skills
from utils.database import create_table, insert_candidate, get_candidates
from models.bert_matcher import bert_match
create_table()


col1, col2 = st.columns([4,1])


with col1:
    st.title("AI Resume Screening System")



with st.sidebar:

    st.title("AI Resume Screening")

    st.markdown("---")

    page = st.radio(
        "Navigation",
        [
            "Resume Screening",
            "Analytics Dashboard",
            "Reports"
        ]
    )

    st.markdown("---")

    st.info(
        "AI-powered recruitment and resume screening system."
    )
resumes = st.file_uploader(
    "Upload Resumes (PDF)",
    type=["pdf"],
    accept_multiple_files=True,
    key="resume_upload"
)

job_description = st.text_area(
    "Paste Job Description"
)

if st.button("Analyze Resume"):

    if resumes and job_description:

        for resume in resumes:

            resume_text = extract_text(resume)

            resume_skills = extract_skills(resume_text)

            jd_skills = extract_skills(job_description)

            # Calculate score
            score = bert_match(
                resume_text,
                job_description
            )

            # Handle None values
            if score is None:
                score = 0

            score = float(score)

            # Missing skills
            missing_skills = list(
                set(jd_skills) - set(resume_skills)
            )

            # Recommendation
            if score >= 80:
                recommendation = "Highly Recommended"

            elif score >= 60:
                recommendation = "Recommended"

            elif score >= 40:
                recommendation = "Consider"

            else:
                recommendation = "Not Suitable"

            # Save candidate
            insert_candidate(
                resume.name,
                ",".join(resume_skills),
                score,
                recommendation
            )

        st.success("All resumes analyzed successfully!")

    else:
        st.warning(
            "Please upload resume and enter job description."
        )
st.markdown("""
<h2 style="
color:#1E293B;
padding:10px 0;
">
📊 Recruiter Dashboard
</h2>
""", unsafe_allow_html=True)

data = get_candidates()

if data:

    df = pd.DataFrame(
        data,
        columns=[
            "ID",
            "Name",
            "Skills",
            "Score",
            "Recommendation"
        ]
    )

    # Dashboard Metrics
    total_candidates = len(df)

    df["Score"] = pd.to_numeric(
        df["Score"],
        errors="coerce"
    )

    df["Score"] = df["Score"].fillna(0)

    avg_score = round(
    df["Score"].mean(),
    2
    )

    top_candidate = df.loc[
        df["Score"].idxmax(),
        "Name"
    ]
    col1, col2, col3 = st.columns(3)

    col1.markdown(f"""
    <div style="
    background:white;
    padding:25px;
    border-radius:18px;
    box-shadow:0px 6px 20px rgba(0,0,0,0.1);
    text-align:center;
    ">
    <h4 style="color:#6366F1;">👥 Total Candidates</h4>
    <h1 style="color:#111827;">{total_candidates}</h1>
    </div>
    """, unsafe_allow_html=True)

    col2.markdown(f"""
    <div style="
    background:white;
    padding:25px;
    border-radius:18px;
    box-shadow:0px 6px 20px rgba(0,0,0,0.1);
    text-align:center;
    ">
    <h4 style="color:#F59E0B;">⭐ Average Score</h4>
    <h1 style="color:#111827;">{avg_score}%</h1>
    </div>
    """, unsafe_allow_html=True)

    col3.markdown(f"""
    <div style="
    background:white;
    padding:25px;
    border-radius:18px;
    box-shadow:0px 6px 20px rgba(0,0,0,0.1);
    text-align:center;
    ">
    <h4 style="color:#10B981;">🏆 Top Candidate</h4>
    <h3 style="color:#111827;">{top_candidate}</h3>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("🏆 Candidate Ranking")
    st.dataframe(df)

    # Excel Download

    excel_file = "candidate_report.xlsx"

    df.to_excel(
        excel_file,
        index=False
    )

    with open(excel_file, "rb") as file:

        st.download_button(
            label="📥 Download Excel Report",
            data=file,
            file_name="candidate_report.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

    # Bar Chart

    st.subheader("📈 Candidate Scores")

    fig = px.bar(
        df,
        x="Name",
        y="Score",
        color="Score",
        title="Candidate Match Scores"
    )

    fig.update_layout(
        paper_bgcolor="white",
        plot_bgcolor="white",
        title_font_size=22
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # Pie Chart

    st.subheader("🥧 Recommendation Distribution")

    pie = px.pie(
        df,
        names="Recommendation",
        title="Recommendation Breakdown"
    )

    st.plotly_chart(
        pie,
        use_container_width=True
    )
