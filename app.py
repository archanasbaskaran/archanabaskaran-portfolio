import streamlit as st
import base64

# --- PAGE CONFIG ---
st.set_page_config(page_title="Archana Baskaran", layout="wide")

# --- TABS ---
tab1, tab2, tab3, tab4 = st.tabs(["👤 About Me", "🛠 Skills", "💼 Experience", "📂 Projects"])

# ============================================================
# TAB 1 — ABOUT ME
# ============================================================
with tab1:
    st.title("Archana Baskaran")
    st.subheader("BIS Health Informatics (Georgia State) | MS Data Analytics (Georgia Tech)")
    st.write("Atlanta, GA | achusbaski@gmail.com | [LinkedIn](https://www.linkedin.com/in/archana-baskaran-2a605517b/)")
  
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("Profile_Pic.JPG", use_column_width=True)
    with col2:
        st.header("About Me")
        st.write("""
        Data Analyst with experience across SaaS, federal agencies, and academic projects.
        Skilled in SQL, Python, R, Tableau, and cloud technologies with strengths in
        dashboarding, machine learning, and NLP. Passionate about transforming data
        into clear, actionable insights.
        """)

# ============================================================
# TAB 2 — SKILLS
# ============================================================
with tab2:
    st.header("Technical Skills")
    col3, col4 = st.columns(2)

    with col3:
        st.write("""
        **Languages:** Python, R, SQL, SAS  
        **Analytics Tools:** Tableau, Power BI, DOMO, Excel  
        """)

    with col4:
        st.write("""
        **Cloud:** AWS, GCP  
        **ML/NLP:** BERT, VADER, DNN, FAISS  
        **Other:** Docker, Arena Simulation  
        """)

# ============================================================
# TAB 3 — EXPERIENCE
# ============================================================
with tab3:
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

# ============================================================
# TAB 4 — PROJECTS
# ============================================================
with tab4:
    st.header("Projects")

    st.subheader("🔹 Sentiment Analysis for School Board Communications (May–Jul 2025)")
    st.write("""
    NLP pipeline analyzing public education sentiment with real-time Power BI updates.
    """)

    st.subheader("🔹 Hybrid STR Recommendation System (Jan–May 2025)")
    st.write("""
    Built a hybrid DNN + BERT + FAISS recommendation engine.
    Achieved 85% perceived relevance from user testing.
    """)

    st.subheader("🔹 Oil Well Drilling Optimization (Aug–Dec 2024)")
    st.write("""
    Performed EDA and modeling to identify ROP drivers; produced a cost model
    estimating $5.6M savings over 20 years.
    """)

    # --- OPTIONAL: Add PDF Viewer for Team Report ---
    try:
        with open("team079report.pdf", "rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode("utf-8")

        st.subheader("📄 Team 079 Report")
        st.components.v1.html(
            f"""
            <iframe src="data:application/pdf;base64,{base64_pdf}"
                    width="100%" height="700" type="application/pdf">
            </iframe>
            """,
            height=700,
        )
    except:
        st.info("Upload **team079report.pdf** to your repo to display it here.")











