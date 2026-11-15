import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

from utils.data_loader import load_energy_data

# PAGE CONFIGURATION
st.set_page_config(
    page_title="Energy Dashboard",
    page_icon="📊",
    layout="wide"
)

# LOAD DESIGN
css_path = Path(__file__).parent.parent / "styles" / "style.css"

if css_path.exists():
    st.markdown(
        f"<style>{css_path.read_text(encoding='utf-8')}</style>",
        unsafe_allow_html=True
    )

# LOAD ACTUAL EXCEL DATA
try:
    df = load_energy_data()
except Exception as e:
    st.error(f"Unable to load the Excel dataset: {e}")
    st.stop()

if df.empty:
    st.warning("No valid energy records were found.")
    st.stop()

# PREPARE DATA
df["consumption_source"] = (
    df["consumption_source"].astype(str).str.strip().str.title()
)

df["peak_consumption"] = (
    df["peak_consumption"]
    .astype(str)
    .str.strip()
    .str.lower()
    .isin(["true", "1", "yes"])
)

df = df.sort_values("timestamp")

# PAGE TITLE
st.title("📊 Energy Monitoring Dashboard")
st.caption(
    "Monitor electricity consumption and understand "
    "your energy usage using the actual project dataset."
)

st.success(f"Successfully loaded {len(df)} energy records.")

# SIDEBAR FILTERS
st.sidebar.divider()
st.sidebar.subheader("Dashboard Filters")

date_options = {
    "All Records": None,
    "Last 7 Days": 7,
    "Last 30 Days": 30
}

selected_period = st.sidebar.selectbox(
    "Select time period",
    list(date_options.keys())
)

days = date_options[selected_period]

if days is None:
    filtered_df = df.copy()
else:
    latest_date = df["timestamp"].max()
    start_date = latest_date - pd.Timedelta(days=days)
    filtered_df = df[df["timestamp"] >= start_date].copy()

if filtered_df.empty:
    st.warning("No records available for this time period.")
    st.stop()

# CALCULATIONS
total_energy = filtered_df["consumption_kwh"].sum()
average_energy = filtered_df["consumption_kwh"].mean()
record_count = len(filtered_df)

peak_count = filtered_df["peak_consumption"].sum()
peak_percentage = (peak_count / record_count) * 100

# ELECTRICITY TARIFF
st.sidebar.divider()
rate = st.sidebar.number_input(
    "Electricity rate (₹ per kWh)",
    min_value=0.0,
    value=8.0,
    step=0.5
)

estimated_cost = total_energy * rate

# DAILY SUMMARY
daily_data = (
    filtered_df.groupby(
        filtered_df["timestamp"].dt.date
    )["consumption_kwh"]
    .sum()
    .reset_index()
)

daily_data.columns = ["Date", "Consumption"]
daily_average = daily_data["Consumption"].mean()

# ENERGY OVERVIEW
st.markdown(
    '<div class="section-heading">Energy Overview</div>',
    unsafe_allow_html=True
)

c1, c2, c3, c4 = st.columns(4)

metrics = [
    (c1, "⚡", "Total Consumption", f"{total_energy:,.2f} kWh"),
    (c2, "📅", "Average per Record", f"{average_energy:,.2f} kWh"),
    (c3, "💰", "Estimated Cost", f"₹{estimated_cost:,.2f}"),
    (c4, "📈", "Peak Records", f"{peak_percentage:.1f}%")
]

for col, icon, label, value in metrics:
    with col:
        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-icon">{icon}</div>
                <div class="metric-label">{label}</div>
                <div class="metric-value">{value}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

st.caption(
    f"Daily average consumption: {daily_average:,.2f} kWh | "
    f"Records analysed: {record_count}"
)

# DAILY CONSUMPTION GRAPH
st.markdown(
    '<div class="section-heading">Daily Energy Consumption</div>',
    unsafe_allow_html=True
)

st.caption("Total electricity consumption recorded each day.")

chart_data = daily_data.set_index("Date")

st.line_chart(
    chart_data,
    y="Consumption",
    x_label="Date",
    y_label="Energy (kWh)"
)

# ENERGY SOURCE ANALYSIS
st.markdown(
    '<div class="section-heading">Energy Source Analysis</div>',
    unsafe_allow_html=True
)

source_totals = (
    filtered_df.groupby("consumption_source")["consumption_kwh"]
    .sum()
    .sort_values(ascending=False)
)

left, right = st.columns(2)

with left:
    st.markdown("#### Consumption Distribution")

    fig, ax = plt.subplots(figsize=(6, 4))

    ax.pie(
        source_totals,
        labels=source_totals.index,
        autopct="%1.1f%%",
        startangle=90
    )

    ax.set_title("Energy Usage by Source")
    st.pyplot(fig)
    plt.close(fig)

with right:
    st.markdown("#### Source Comparison")

    st.bar_chart(
        source_totals,
        horizontal=True,
        x_label="Energy (kWh)"
    )

# ENERGY INSIGHTS
st.markdown(
    '<div class="section-heading">💡 Energy Insights</div>',
    unsafe_allow_html=True
)

highest_source = source_totals.idxmax()
highest_value = source_totals.max()

st.info(
    f"{highest_source} is the largest contributor to recorded "
    f"energy consumption, with {highest_value:,.2f} kWh."
)

st.write(
    f"Out of {record_count} records, {int(peak_count)} "
    f"are marked as peak consumption records."
)

zero_count = (
    filtered_df["consumption_kwh"] == 0
).sum()

st.write(
    f"Zero-consumption records in this period: {zero_count}"
)

# DATA TABLE
with st.expander("View Energy Consumption Records"):
    st.dataframe(
        filtered_df,
        use_container_width=True,
        hide_index=True
    )

# FOOTER
st.markdown(
    '<div class="footer">ENERGY SAVER | Energy Monitoring Dashboard</div>',
    unsafe_allow_html=True
)