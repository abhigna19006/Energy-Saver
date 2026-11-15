import streamlit as st
from pathlib import Path

# ---------------- PAGE SETTINGS ----------------

st.set_page_config(
    page_title="Energy Saver | Smart Energy",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- LOAD CSS ----------------

css_path = Path(__file__).parent / "styles" / "style.css"

if css_path.exists():
    st.markdown(
        f"<style>{css_path.read_text(encoding='utf-8')}</style>",
        unsafe_allow_html=True
    )

# ---------------- SIDEBAR ----------------

with st.sidebar:
    st.markdown("## ⚡ ENERGY SAVER")
    st.caption("SMART ENERGY MANAGEMENT")

    st.divider()

    st.markdown("### Navigation")
    st.markdown("🏠  Home")
    st.markdown("📊  Dashboard")
    st.markdown("📈  Energy Analysis")
    st.markdown("🤖  AI Detection")
    st.markdown("💬  Energy Bot")
    st.markdown("💡  Recommendations")
    st.markdown("📄  About Project")

    st.divider()

    st.markdown("### Project Status")
    st.success("Prototype Development")

    st.caption("Smart energy. Better tomorrow.")

# ---------------- HERO SECTION ----------------

st.markdown(
    """
    <div class="hero">
        <div class="hero-tag">⚡ SMART ENERGY MANAGEMENT PLATFORM</div>
        <h1>Power Smarter.<br>Live Greener.</h1>
        <p>
            Take control of electricity consumption with intelligent
            monitoring, data-driven insights, unusual usage detection,
            and practical energy-saving recommendations.
        </p>
        <div class="hero-icon">🌱</div>
    </div>
    """,
    unsafe_allow_html=True
)

# ---------------- WELCOME ----------------

st.markdown(
    '<div class="section-heading">Welcome to Energy Saver</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-subtitle">'
    'A smarter approach to understanding and reducing electricity waste.'
    '</div>',
    unsafe_allow_html=True
)

# ---------------- METRIC CARDS ----------------

col1, col2, col3 = st.columns(3)

metrics = [
    ("⚡", "Energy Monitoring", "Understand electricity usage"),
    ("🧠", "AI-Powered Insights", "Identify unusual usage patterns"),
    ("🌿", "Smart Recommendations", "Discover ways to save energy")
]

for column, metric in zip([col1, col2, col3], metrics):
    icon, title, description = metric

    with column:
        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-icon">{icon}</div>
                <div class="metric-label">{title}</div>
                <div style="font-size:14px;color:#718078;margin-top:8px;">
                    {description}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

# ---------------- FEATURES ----------------

st.markdown(
    '<div class="section-heading">Explore Our Features</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-subtitle">'
    'Everything you need for smarter energy management.'
    '</div>',
    unsafe_allow_html=True
)

features = [
    ("📊", "Energy Dashboard",
     "View consumption summaries and electricity usage trends."),
    ("📈", "Energy Analysis",
     "Explore daily usage and appliance-wise energy patterns."),
    ("🧠", "AI Waste Detection",
     "Detect unusual energy consumption for further review."),
    ("💬", "Energy Saver Bot",
     "Ask questions and get practical electricity-saving guidance."),
    ("💡", "Smart Recommendations",
     "Discover useful ideas to reduce electricity consumption."),
    ("📄", "Reports & Insights",
     "Understand energy patterns through meaningful summaries.")
]

for start in range(0, len(features), 3):
    cols = st.columns(3)

    for col, feature in zip(cols, features[start:start + 3]):
        icon, title, description = feature

        with col:
            st.markdown(
                f"""
                <div class="feature-card">
                    <div class="feature-icon">{icon}</div>
                    <div class="feature-title">{title}</div>
                    <div class="feature-description">{description}</div>
                </div>
                """,
                unsafe_allow_html=True
            )

st.markdown(
    """
    <div class="footer">
        ENERGY SAVER · Smart Energy Consumption and Electricity Waste Reduction
        <br><br>
        Academic Project | Built with Python and Streamlit
    </div>
    """,
    unsafe_allow_html=True
)