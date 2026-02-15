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
        Hello, I'm a recent Master’s graduate in Analytics from Georgia Tech, with an undergraduate background in Health Informatics from Georgia State. 
        I have hands-on experience building data-driven projects using Python, R, SQL, Tableau and PowerBI, and I enjoy transforming complex data into clear insights through analysis and visualization. 
        I have hands-on experience building data-driven projects using Python, R, SQL, Tableau, and PowerBI, and I enjoy transforming complex data into clear insights through analysis and visualization. 
        With a strong interdisciplinary foundation and practical project experience, I’m eager to grow into a data-focused role and continue creating meaningful impact ⭐
        """)
# ============================================================
# TAB 2 — SKILLS
# ============================================================


# ============================================================
# TAB 3 — EXPERIENCE
# ============================================================
with tab2:
    st.header("Experience")

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

    st.subheader("🔹 Ranking and Selection Project (May–Jul 2025)")
    st.write("""
    Implemented an R-based simulation using Bechhofer’s Ranking and Selection method to identify the best-performing queueing system.
    """)
    try:
        with open("Simulation Project.pdf", "rb") as f:
             pdf_bytes = f.read()

        st.download_button(
            label="⬇️ Download Project Report (PDF)",
            data=pdf_bytes,
            file_name= "Simulation Project.pdf",
            mime="application/pdf"
    )

    except FileNotFoundError:
        st.info("Upload **Simulation Project.pdf** to your repository to enable download.")
    
    st.subheader("🔹 Hybrid STR Recommendation System (Jan–May 2025)")
    st.write("""
    Built a hybrid DNN + BERT + FAISS recommendation engine.
    Achieved 85% perceived relevance from user testing.
    """)
    try:
        with open("STR Project.pdf", "rb") as f:
             pdf_bytes = f.read()

        st.download_button(
            label="⬇️ Download Project Report (PDF)",
            data=pdf_bytes,
            file_name= "STR Project.pdf",
            mime="application/pdf"
    )

    except FileNotFoundError:
        st.info("Upload **STR Project.pdf** to your repository to enable download.")

    
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

















































