import streamlit as st


st.set_page_config(page_title="Archana Baskaran", layout="wide")

# --- HEADER ---
st.title("💼 Archana Baskaran")
st.subheader("BIS Health Informatics (Georgia State) | MS Data Analytics (Georgia Tech)")
st.write("Atlanta, GA | achusbaski@gmail.com | [LinkedIn](https://www.linkedin.com/in/archana-baskaran-2a605517b/)")

st.markdown("---")  # changed from st.divider()

# --- SUMMARY ---
st.header("Summary")
st.write("""
Data Analyst with experience across SaaS, federal agencies, and academic projects.
Skilled in SQL, Python, R, Tableau, and cloud technologies with strengths in
dashboarding, machine learning, and NLP. Passionate about transforming data
into clear, actionable insights.
""")

st.markdown("---")  # changed from st.divider()

# --- SKILLS ---
st.header("Technical Skills")
col1, col2 = st.columns(2)

with col1:
    st.write("""
**Languages:** Python, R, SQL, SAS  
**Analytics Tools:** Tableau, Power BI, DOMO, Excel  
""")

with col2:
    st.write("""
**Cloud:** AWS, GCP  
**ML/NLP:** BERT, VADER, DNN, FAISS  
**Other:** Docker, Arena Simulation  
""")

st.markdown("---")  # changed from st.divider()

# --- EXPERIENCE ---
st.header("Experience")

st.subheader("📌 Informatics Fellow – CDC (Oct 2024–Mar 2025)")
st.write("""
- Worked with metadata to extract relevant clinical features and built interactive dashboards
- Applied AI/ML and NLP to gain insights from quantitative and qualitative clinical and epidemiological data
- Conducted risk modeling, simulation, and performance measurement across public health programs 
""")

st.subheader("📌 Data Analyst Intern – Infor (May 2024–Aug 2024)")
st.write("""
- Streamlined 20+ dashboards, reducing reporting redundancy across sales & marketing  
- Built DOMO cards for Sales Play V2 dashboard  
- Supported iCRM → Salesforce migration with ETL/EDW field mapping  
- Delivered KPI inventory & adoption analysis for 5+ dashboards  
""")

st.subheader("📌 Data Intern – ASPR (Aug 2022–May 2023)")
st.write("""
- Built outcome indicators evaluating long-term healthcare interventions  
- Cleaned multi-state datasets using R  
- Identified data sources for 10+ states  
- Created public-facing data resource guides  
""")

st.subheader("📌 Data Analytics Intern – HHS (Aug 2021–May 2022)")
st.write("""
- Analyzed COVID-19 and school-closure data with Tableau & HHS Protect  
- Assessed recovery efforts across states  
- Synthesized 200+ RFI responses on pandemic funding  
- Drafted guidance reports on technology & community-centered innovation  
""")

st.markdown("---")  # changed from st.divider()

# --- PROJECTS ---
st.header("Projects")

st.subheader("🔹 Hybrid STR Recommendation System (Jan–May 2025)")
st.write("""
Built a hybrid DNN + BERT + FAISS recommendation engine.
Achieved 85% perceived relevance from user testing.
""")

st.header("📄 Team 079 Project Report")

with open("team079report.pdf", "rb") as f:
    pdf_data = f.read()

st.download_button(
    label="⬇️ Download Report",
    data=pdf_data,
    file_name="team079report.pdf",
    mime="application/pdf",
)
#--
st.subheader("🔹 Sentiment Analysis for School Board Communications (May–Jul 2025)")
st.write("""
NLP pipeline analyzing public education sentiment with real-time Power BI updates.
""")

st.subheader("🔹 Oil Well Drilling Optimization (Aug–Dec 2024)")
st.write("""
Performed EDA and modeling to identify ROP drivers; produced a cost model
estimating $5.6M savings over 20 years.
""")

st.markdown("---")  # changed from st.divider()







