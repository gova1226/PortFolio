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
🔗 [LinkedIn](https://www.linkedin.com/in/govardhanan-g-1b2770102/) | 
💻 [GitHub](https://github.com/gova1226)
""")

st.divider()

# -------------------- SUMMARY --------------------
st.header("Professional Summary")

st.write("""
Data Analyst with 4+ years of hands-on experience in data analysis, and 7+ years of overall professional experience across analytics, operations, and reporting automation.
Strong expertise in SQL, Python (Pandas, NumPy), Power BI, and Streamlit for exploratory data analysis (EDA), dashboard development, and business insights.
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

with st.expander("📌 Airbnb Data Analysis and Visualization"):
    st.write("""
    **Role:** Data Analyst  
    **Tools:** Python, Pandas, Streamlit, Matplotlib, Seaborn  

    - Performed exploratory data analysis (EDA) on Airbnb listings to analyze pricing, availability, and neighborhood trends  
    - Cleaned and transformed data to handle missing values and outliers  
    - Identified key factors influencing price variation across locations  
    - Built interactive dashboards using Streamlit for insight-driven exploration  
    - Improved insight generation efficiency by 35%  
    """)

with st.expander("📌 Industrial Copper Data Analysis and Modeling"):
    st.write("""
    **Role:** Data Analyst (Predictive Analytics)  
    **Tools:** Python, Pandas, Scikit-learn, Streamlit  

    - Analyzed manufacturing sales data to understand pricing and lead conversion behavior  
    - Handled skewed and noisy data using preprocessing and transformation techniques  
    - Performed exploratory analysis to uncover pricing patterns  
    - Built regression and classification models to support business decisions  
    - Improved pricing accuracy and lead evaluation efficiency by 40%  
    """)

with st.expander("📌 Singapore Resale Flat Prices Analysis"):
    st.write("""
    **Role:** Data Analyst  
    **Tools:** Python, Pandas, Scikit-learn, Streamlit  

    - Analyzed Singapore HDB resale flat data to identify pricing trends and key drivers  
    - Performed feature engineering on property attributes  
    - Built regression-based models for price forecasting  
    - Developed a Streamlit interface for interactive price estimation  
    - Improved pricing insight generation by 30%  
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



