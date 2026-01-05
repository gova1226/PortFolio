import streamlit as st

# Page config
st.set_page_config(
    page_title="Govardhanan G | Data Analyst Portfolio",
    page_icon="📊",
    layout="wide"
)

# -------------------- HEADER --------------------
st.title("📊 Govardhanan G")
st.subheader("Data Analyst | SQL, Python, Power BI | Dashboarding & Business Insights")

st.markdown("""
📍 Coimbatore, Tamil Nadu  
📧 govardhananprema@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/govardhanan-g-1b277010) | 
💻 [GitHub](https://github.com/gova1226)
""")

st.divider()

# -------------------- SUMMARY --------------------
st.header("Professional Summary")

st.write("""
Data Analyst with 7+ years of experience in data analysis, reporting automation, dashboard development, 
and KPI tracking. Strong expertise in SQL, Python (Pandas, NumPy), Power BI, and Streamlit for exploratory 
data analysis (EDA), data visualization, and business insights. Proven ability to automate reporting workflows, 
improve data accuracy, and support data-driven decision-making across operations and analytics teams.
""")

# -------------------- SKILLS --------------------
st.header("Technical Skills")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Data Analysis & Programming")
    st.write("""
    - SQL  
    - Python  
    - Pandas, NumPy  
    - Exploratory Data Analysis (EDA)  
    - Data Cleaning & Transformation
    """)

with col2:
    st.subheader("Databases & BI")
    st.write("""
    - MySQL  
    - PostgreSQL  
    - SQLite  
    - Power BI  
    - Dashboard Development
    """)

with col3:
    st.subheader("Visualization & Tools")
    st.write("""
    - Streamlit  
    - Plotly  
    - Matplotlib  
    - Seaborn  
    - Git & GitHub
    """)

# -------------------- PROJECTS --------------------
st.header("Projects")

with st.expander("📌 YouTube Data Harvesting and Analysis"):
    st.write("""
    **Role:** Data Analyst  
    **Tools:** SQL, Python, Pandas, MySQL, Streamlit  

    - Collected and cleaned YouTube channel, video, and comment data using APIs  
    - Designed a relational database in MySQL for structured analysis  
    - Performed EDA to identify engagement trends and performance KPIs  
    - Built interactive dashboards for views, likes, comments, and upload frequency  
    - Enabled ad-hoc SQL queries for faster reporting and insights  
    """)

with st.expander("📌 PhonePe Pulse – Transaction Data Analysis"):
    st.write("""
    **Role:** Data Analyst  
    **Tools:** Python, SQL, Pandas, Streamlit, Plotly  

    - Analyzed large-scale digital payment transaction data across India  
    - Cleaned, transformed, and aggregated datasets for reporting  
    - Built dashboards for transaction volume, value, and growth trends  
    - Performed time-series and regional analysis  
    - Reduced manual data exploration time by 50%  
    """)

with st.expander("📌 Customer Churn Analysis – Publishing Industry"):
    st.write("""
    **Role:** Data Analyst (Predictive Analytics)  
    **Tools:** Python, Pandas, SQL, Streamlit  

    - Conducted EDA to identify key churn drivers  
    - Performed feature engineering and metric evaluation  
    - Built dashboards to visualize churn probability and customer segments  
    - Supported data-driven retention strategies  
    """)

# -------------------- EXPERIENCE --------------------
st.header("Professional Experience")

st.subheader("Senior Software Engineer – TechOps")
st.caption("ADF Data Science Pvt Ltd | Apr 2022 – Present")

st.write("""
- Analyzed operational datasets to identify workflow bottlenecks, reducing delays by 30%  
- Automated SQL and Excel-based reporting, reducing manual effort by 40%  
- Built standardized KPI reports and dashboards  
- Improved reporting accuracy and consistency by 20%  
- Collaborated with analytics and compliance teams for data-driven decisions  
""")

st.subheader("Senior Associate – Backend Operations")
st.caption("ADF Data Science Pvt Ltd | Nov 2017 – Apr 2022")

st.write("""
- Reviewed and analyzed high-volume transactional data with 98% accuracy  
- Identified anomalies and risks using structured analysis  
- Maintained data quality and SLA-driven reporting  
""")

# -------------------- EDUCATION --------------------
st.header("Education")

st.write("""
🎓 **Advanced Programming Professional & Master**  
GUVI – IIT Madras (2024)

🎓 **B.E. Computer Science**  
Kathir College of Engineering (2015)
""")

# -------------------- FOOTER --------------------
st.divider()
st.caption("📊 Data Analyst Portfolio | Built with Streamlit")
