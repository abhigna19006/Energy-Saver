import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="About Project | Energy Saver",
    page_icon="⚡",
    layout="wide"
)

ROOT = Path(__file__).parent.parent
css_path = ROOT / "styles" / "style.css"

if css_path.exists():
    st.markdown(
        f"<style>{css_path.read_text(encoding='utf-8')}</style>",
        unsafe_allow_html=True
    )

st.markdown("""
<div class="hero">
    <h1>About Energy Saver ⚡</h1>
    <p>Smart Energy Consumption Monitoring and Electricity Waste Reduction</p>
</div>
""", unsafe_allow_html=True)

st.write("")

st.markdown("## 🌱 Project Overview")

st.write("""
Energy Saver is a smart energy management application designed to help
users understand their electricity consumption, identify unusual usage
patterns, and reduce unnecessary energy wastage.

The application provides interactive dashboards, energy analysis,
AI-based unusual usage detection, and personalized energy-saving
recommendations.
""")

st.markdown("## 🎯 Problem Statement")

st.write("""
Electricity is often wasted because users do not continuously monitor
their energy consumption. Without proper information, it becomes
difficult to identify high-energy-consuming appliances and unusual
usage patterns.

Energy Saver aims to make energy consumption easier to understand
through data analysis and intelligent recommendations.
""")

st.markdown("## 🚀 Project Objectives")

objectives = [
    "Monitor electricity consumption of different appliances.",
    "Display energy usage through interactive charts and dashboards.",
    "Identify unusual electricity consumption patterns using machine learning.",
    "Provide practical recommendations to reduce electricity bills.",
    "Help users develop energy-efficient habits."
]

for item in objectives:
    st.markdown(f"- {item}")

st.markdown("## ⚙️ How the System Works")

steps = [
    ("01", "Energy Data", "Collect appliance-wise electricity consumption data."),
    ("02", "Data Processing", "Organize and analyze the consumption information."),
    ("03", "AI Detection", "Use Isolation Forest to identify unusual usage patterns."),
    ("04", "Recommendations", "Suggest practical ways to reduce electricity consumption."),
    ("05", "Dashboard", "Present results through charts, metrics, and reports.")
]

for number, heading, description in steps:
    st.markdown(f"""
    <div class="feature-card">
        <h3>{number} | {heading}</h3>
        <p>{description}</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("## 🛠️ Technologies Used")

tech_col1, tech_col2 = st.columns(2)

with tech_col1:
    st.markdown("""
    <div class="feature-card">
        <h3>🐍 Python</h3>
        <p>Main programming language used to develop the application.</p>
    </div>
    <div class="feature-card">
        <h3>📊 Pandas</h3>
        <p>Used for handling and analyzing energy consumption data.</p>
    </div>
    <div class="feature-card">
        <h3>🤖 Scikit-learn</h3>
        <p>Used for machine learning-based unusual usage detection.</p>
    </div>
    """, unsafe_allow_html=True)

with tech_col2:
    st.markdown("""
    <div class="feature-card">
        <h3>🌐 Streamlit</h3>
        <p>Used to build the interactive web application.</p>
    </div>
    <div class="feature-card">
        <h3>📈 Matplotlib</h3>
        <p>Used to create visual representations of energy data.</p>
    </div>
    <div class="feature-card">
        <h3>🎨 HTML & CSS</h3>
        <p>Used to improve the application's appearance and styling.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("## ✨ Key Features")

features = [
    "Interactive Energy Dashboard",
    "Appliance-wise Energy Analysis",
    "AI-based Unusual Usage Detection",
    "Energy Saving Chatbot",
    "Personalized Recommendations",
    "Energy Report Download"
]

feature_cols = st.columns(2)

for index, feature in enumerate(features):
    with feature_cols[index % 2]:
        st.markdown(f"""
        <div class="feature-card">
            <p>⚡ {feature}</p>
        </div>
        """, unsafe_allow_html=True)

st.markdown("## 📌 Current Project Scope")

st.info("""
This version uses a cleaned electricity consumption dataset containing 500 records. The system analyses energy consumption, identifies unusual usage patterns using an Isolation Forest model, and provides energy-saving recommendations. AI alerts identify unusual patterns for further investigation; they do not automatically prove electricity wastage, appliance faults or electricity theft. The system does not directly control electrical appliances."
Also, your key features do not require pictures. The feature descriptions are perfectly acceptable.
""")

st.markdown("""
<div class="footer">
    <p>Energy Saver | Power Smarter. Live Greener. 🌍</p>
</div>
""", unsafe_allow_html=True)