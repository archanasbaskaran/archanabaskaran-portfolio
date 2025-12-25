import streamlit as st
import base64

# --- PAGE CONFIG ---
st.set_page_config(page_title="Archana Baskaran", layout="wide")

# --- TABS ---
tab1, tab2, tab3 = st.tabs(["👤 About Me", "💼 Experience", "📂 Projects"])

# ============================================================
# TAB 1 — ABOUT ME
# ============================================================
with tab1:
    st.title("Archana Baskaran")
    st.subheader("BIS Health Informatics (Georgia State) 🐆| MS Data Analytics (Georgia Tech) 🐝")
    st.write("Atlanta, GA | achusbaski@gmail.com | [LinkedIn](https://www.linkedin.com/in/archana-baskaran-2a605517b/)")
  
    col1, col2 = st.columns([1, 2])
    with col1:
       st.image("Profile_Pic.JPG", caption="Archana Baskaran", use_column_width=True)
   
    
    st.markdown("### Technical Skills")
    colA, colB = st.columns(2)

    with colA:
            st.write("""
            **Languages:** Python, R, SQL, SAS  
            **Analytics Tools:** Tableau, Power BI, DOMO, Excel  
            """)

    with colB:
            st.write("""
            **Cloud:** AWS, GCP  
            **ML/NLP:** BERT, VADER, DNN, FAISS  
            **Other:** Docker, Arena Simulation  
            """)

    # Profile picture
    with col2:
        st.header("Summary")
        st.write("""
        Data Analyst with experience across SaaS, federal agencies, and academic projects.
        Skilled in SQL, Python, R, Tableau, and cloud technologies with strengths in
        dashboarding, machine learning, and NLP. Passionate about transforming data
        into clear, actionable insights.
        """)
# ============================================================
# TAB 2 — SKILLS
# ============================================================


# ============================================================
# TAB 3 — EXPERIENCE
# ============================================================
with tab2:
    st.header("Experience")

    st.subheader("🌟 Informatics Fellow – CDC (Oct 2024–Mar 2025)")
    st.write("""
    - Worked with metadata to extract relevant clinical features and built interactive dashboards  
    - Applied AI/ML and NLP to gain insights from quantitative and qualitative clinical and epidemiological data  
    - Conducted risk modeling, simulation, and performance measurement across public health programs  
    """)

    st.subheader("🌟 Data Analyst Intern – Infor (May 2024–Aug 2024)")
    st.write("""
    - Streamlined 20+ dashboards, reducing reporting redundancy across sales & marketing  
    - Built DOMO cards for Sales Play V2 dashboard  
    - Supported iCRM → Salesforce migration with ETL/EDW field mapping  
    - Delivered KPI inventory & adoption analysis for 5+ dashboards  
    """)

    st.subheader("🌟 Data Intern – ASPR (Aug 2022–May 2023)")
    st.write("""
    - Built outcome indicators evaluating long-term healthcare interventions  
    - Cleaned multi-state datasets using R  
    - Identified data sources for 10+ states  
    - Created public-facing data resource guides  
    """)

    st.subheader("🌟 Data Analytics Intern – HHS (Aug 2021–May 2022)")
    st.write("""
    - Analyzed COVID-19 and school-closure data with Tableau & HHS Protect  
    - Assessed recovery efforts across states  
    - Synthesized 200+ RFI responses on pandemic funding  
    - Drafted guidance reports on technology & community-centered innovation  
    """)

# ============================================================
# TAB 4 — PROJECTS
# ============================================================
with tab3:
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
    try:
         with open("Oil Drilling Project.pdf", "rb") as f:
             pdf_bytes = f.read()

        st.download_button(
            label="⬇️ Download Project Report (PDF)",
            data=pdf_bytes,
            file_name= "Oil_Drilling_Project_Report.pdf",
            mime="application/pdf"
    )

    except FileNotFoundError:
        st.info("Upload **Oil Drilling Project.pdf** to your repository to enable download.")

































