import streamlit as st
import pandas as pd
from pathlib import Path

# PAGE CONFIGURATION
st.set_page_config(
    page_title="Smart Recommendations",
    page_icon="💡",
    layout="wide"
)

# LOAD CSS AND DATA
ROOT = Path(__file__).resolve().parents[1]

css_path = ROOT / "styles" / "style.css"

if css_path.exists():
    st.markdown(
        f"<style>{css_path.read_text(encoding='utf-8')}</style>",
        unsafe_allow_html=True
    )

from utils.data_loader import load_energy_data

# LOAD ACTUAL DATASET
try:
    energy_data = load_energy_data()
except Exception as e:
    st.error(f"Unable to load the energy dataset: {e}")
    st.stop()

# HEADER
st.title("💡 Smart Energy Recommendations")
st.caption(
    "Understand energy consumption and discover practical "
    "ways to reduce electricity usage."
)

st.divider()

# INTRODUCTION
st.markdown(
    """
    <div class="hero">
        <div class="hero-tag">🌱 INTELLIGENT ENERGY SAVING</div>
        <h1>Small Changes.<br>Big Energy Savings.</h1>
        <p>
            Analyze your actual energy dataset and explore
            personalized appliance-saving estimates.
        </p>
        <div class="hero-icon">💡</div>
    </div>
    """,
    unsafe_allow_html=True
)

# ACTUAL DATASET SUMMARY
st.markdown(
    '<div class="section-heading">Actual Dataset Overview</div>',
    unsafe_allow_html=True
)

total_records = len(energy_data)
total_consumption = energy_data["consumption_kwh"].sum()
average_consumption = energy_data["consumption_kwh"].mean()
peak_records = int(energy_data["peak_consumption"].sum())

c1, c2, c3 = st.columns(3)

with c1:
    st.metric("Dataset Records", f"{total_records}")

with c2:
    st.metric("Total Consumption", f"{total_consumption:,.2f} kWh")

with c3:
    st.metric("Average Consumption", f"{average_consumption:.2f} kWh")

st.caption(
    f"Peak consumption records: {peak_records} "
    f"out of {total_records} records."
)

# SOURCE ANALYSIS
st.markdown(
    '<div class="section-heading">Energy Source Analysis</div>',
    unsafe_allow_html=True
)

source_summary = (
    energy_data.groupby("consumption_source")["consumption_kwh"]
    .sum()
    .reset_index()
    .sort_values("consumption_kwh", ascending=False)
)

left, right = st.columns(2)

with left:
    st.markdown("#### Consumption by Energy Source")
    st.bar_chart(
        source_summary.set_index("consumption_source")
    )

with right:
    st.markdown("#### Energy Source Details")
    st.dataframe(
        source_summary,
        use_container_width=True,
        hide_index=True
    )

# DATASET-BASED RECOMMENDATIONS
st.markdown(
    '<div class="section-heading">Dataset-Based Recommendations</div>',
    unsafe_allow_html=True
)

grid_records = energy_data[
    energy_data["consumption_source"].str.lower() == "grid"
]

solar_records = energy_data[
    energy_data["consumption_source"].str.lower() == "solar"
]

if not grid_records.empty:
    st.markdown(
        """
        <div class="feature-card">
            <div class="feature-title">⚡ Grid Electricity</div>
            <div class="feature-description">
                Monitor grid electricity consumption and reduce
                unnecessary appliance usage. Make efficient use
                of available alternative energy sources.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

if not solar_records.empty:
    st.markdown(
        """
        <div class="feature-card">
            <div class="feature-title">☀️ Solar Energy</div>
            <div class="feature-description">
                Make effective use of available solar electricity
                and monitor solar energy generation and consumption.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

if peak_records > 0:
    st.markdown(
        """
        <div class="feature-card">
            <div class="feature-title">📊 Peak Consumption</div>
            <div class="feature-description">
                Review records marked as peak consumption.
                Identify high-usage periods and avoid unnecessary
                electricity consumption.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# MANUAL APPLIANCE ESTIMATES
st.markdown(
    '<div class="section-heading">Manual Appliance Consumption Estimates</div>',
    unsafe_allow_html=True
)

st.info(
    "Your uploaded dataset does not contain individual appliance "
    "readings. Enter estimated monthly values below to explore "
    "possible appliance-level savings. These estimates are separate "
    "from the actual dataset analysis above."
)

col1, col2 = st.columns(2)

with col1:
    fan = st.number_input(
        "🌀 Fan consumption (kWh/month)",
        min_value=0.0,
        max_value=5000.0,
        value=75.0,
        step=5.0
    )

    lights = st.number_input(
        "💡 Lighting consumption (kWh/month)",
        min_value=0.0,
        max_value=5000.0,
        value=36.0,
        step=5.0
    )

    ac = st.number_input(
        "❄️ AC consumption (kWh/month)",
        min_value=0.0,
        max_value=5000.0,
        value=150.0,
        step=5.0
    )

with col2:
    fridge = st.number_input(
        "🧊 Refrigerator consumption (kWh/month)",
        min_value=0.0,
        max_value=5000.0,
        value=45.0,
        step=5.0
    )

    washing = st.number_input(
        "🧺 Washing machine consumption (kWh/month)",
        min_value=0.0,
        max_value=5000.0,
        value=12.0,
        step=2.0
    )

    other = st.number_input(
        "🔌 Other appliances (kWh/month)",
        min_value=0.0,
        max_value=5000.0,
        value=30.0,
        step=5.0
    )

# CALCULATION SETTINGS
st.markdown(
    '<div class="section-heading">Calculation Settings</div>',
    unsafe_allow_html=True
)

electricity_rate = st.number_input(
    "Estimated electricity rate (₹ per kWh)",
    min_value=0.0,
    max_value=1000.0,
    value=8.0,
    step=0.5
)

saving_target = st.slider(
    "Your desired energy reduction target",
    min_value=5,
    max_value=30,
    value=15,
    step=5
)

# CALCULATIONS
appliance_data = {
    "Fan": fan,
    "Lights": lights,
    "AC": ac,
    "Refrigerator": fridge,
    "Washing Machine": washing,
    "Other Appliances": other
}

df = pd.DataFrame({
    "Appliance": list(appliance_data.keys()),
    "Monthly Consumption (kWh)": list(appliance_data.values())
})

total_energy = sum(appliance_data.values())
monthly_cost = total_energy * electricity_rate
daily_average = total_energy / 30

potential_saving = total_energy * saving_target / 100
potential_cost_saving = potential_saving * electricity_rate

# APPLIANCE OVERVIEW
st.markdown(
    '<div class="section-heading">Estimated Appliance Overview</div>',
    unsafe_allow_html=True
)

c1, c2, c3 = st.columns(3)

with c1:
    st.metric("Estimated Monthly Usage", f"{total_energy:.2f} kWh")

with c2:
    st.metric("Estimated Monthly Cost", f"₹{monthly_cost:.2f}")

with c3:
    st.metric("Potential Monthly Savings", f"₹{potential_cost_saving:.2f}")

st.caption(f"Estimated daily usage: {daily_average:.2f} kWh")

# APPLIANCE ANALYSIS
st.markdown(
    '<div class="section-heading">Appliance Consumption Analysis</div>',
    unsafe_allow_html=True
)

left, right = st.columns(2)

with left:
    st.markdown("#### Monthly Usage Comparison")
    st.bar_chart(
        df.set_index("Appliance"),
        horizontal=True
    )

with right:
    st.markdown("#### Consumption Details")
    st.dataframe(
        df.sort_values(
            "Monthly Consumption (kWh)",
            ascending=False
        ),
        use_container_width=True,
        hide_index=True
    )

# PERSONALIZED RECOMMENDATIONS
st.markdown(
    '<div class="section-heading">🎯 Personalized Recommendations</div>',
    unsafe_allow_html=True
)

recommendations = []

if total_energy == 0:
    st.info("Enter appliance consumption to generate recommendations.")

else:
    highest_appliance = max(appliance_data, key=appliance_data.get)
    highest_usage = appliance_data[highest_appliance]

    recommendations.append((
        "🔍 Highest Consumption",
        f"{highest_appliance} has the highest estimated consumption "
        f"at {highest_usage:.2f} kWh per month. Review its usage habits."
    ))

    if ac > 0:
        recommendations.append((
            "❄️ Air Conditioner",
            "Set a comfortable temperature, clean filters regularly, "
            "and keep doors and windows closed while cooling."
        ))

    if fan > 0:
        recommendations.append((
            "🌀 Fan",
            "Switch off fans in empty rooms and clean fan blades regularly."
        ))

    if lights > 0:
        recommendations.append((
            "💡 Lighting",
            "Replace inefficient bulbs with LEDs and use natural daylight."
        ))

    if fridge > 0:
        recommendations.append((
            "🧊 Refrigerator",
            "Check door seals, avoid frequent opening, and maintain "
            "suitable temperature settings."
        ))

    if washing > 0:
        recommendations.append((
            "🧺 Washing Machine",
            "Run full loads when practical and avoid unnecessary wash cycles."
        ))

    for title, description in recommendations:
        st.markdown(
            f"""
            <div class="feature-card" style="margin-bottom:12px;">
                <div class="feature-title">{title}</div>
                <div class="feature-description">{description}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

# SAVINGS GOAL
st.markdown(
    '<div class="section-heading">Your Energy Saving Goal</div>',
    unsafe_allow_html=True
)

if total_energy > 0:
    st.progress(saving_target / 100)

    st.success(
        f"If you reduce estimated appliance consumption by "
        f"{saving_target}%, you could save approximately "
        f"{potential_saving:.2f} kWh and "
        f"₹{potential_cost_saving:.2f} per month."
    )

    st.caption("This is a target-based estimate, not a guaranteed saving.")

# DOWNLOAD REPORT
st.markdown(
    '<div class="section-heading">Download Your Analysis</div>',
    unsafe_allow_html=True
)

if total_energy > 0:
    report = df.copy()

    report["Estimated Monthly Cost (₹)"] = (
        report["Monthly Consumption (kWh)"] * electricity_rate
    )

    csv = report.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="📥 Download Energy Analysis Report",
        data=csv,
        file_name="energy_saving_report.csv",
        mime="text/csv"
    )

# FOOTER
st.markdown(
    '<div class="footer">ENERGY SAVER | Smart Recommendations</div>',
    unsafe_allow_html=True
)