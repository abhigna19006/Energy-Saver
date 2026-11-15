import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

from utils.data_loader import load_energy_data

# PAGE CONFIGURATION
st.set_page_config(
    page_title="Energy Analysis",
    page_icon="📈",
    layout="wide"
)

# LOAD CSS DESIGN
css_path = Path(__file__).parent.parent / "styles" / "style.css"

if css_path.exists():
    st.markdown(
        f"<style>{css_path.read_text(encoding='utf-8')}</style>",
        unsafe_allow_html=True
    )

# LOAD ACTUAL DATASET
try:
    df = load_energy_data()
except Exception as e:
    st.error(f"Unable to load the Excel dataset: {e}")
    st.stop()

if df.empty:
    st.warning("No valid energy records found.")
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

# PAGE HEADING
st.title("📈 Energy Consumption Analysis")
st.caption(
    "Explore electricity usage, energy source performance, "
    "and consumption patterns using actual dataset records."
)

st.success(f"Analysing {len(df)} actual energy records.")

# ANALYSIS FILTER
st.sidebar.divider()
st.sidebar.subheader("Analysis Filters")

period = st.sidebar.selectbox(
    "Choose analysis period",
    ["All Records", "Last 7 Days", "Last 30 Days"]
)

if period == "All Records":
    analysis_df = df.copy()
else:
    days = 7 if period == "Last 7 Days" else 30
    latest_date = df["timestamp"].max()
    start_date = latest_date - pd.Timedelta(days=days)
    analysis_df = df[
        df["timestamp"] >= start_date
    ].copy()

if analysis_df.empty:
    st.warning("No records available for this period.")
    st.stop()

# CALCULATIONS
total = analysis_df["consumption_kwh"].sum()
average = analysis_df["consumption_kwh"].mean()
maximum = analysis_df["consumption_kwh"].max()
minimum = analysis_df["consumption_kwh"].min()

highest_record = analysis_df.loc[
    analysis_df["consumption_kwh"].idxmax()
]

source_totals = (
    analysis_df.groupby("consumption_source")["consumption_kwh"]
    .sum()
    .sort_values(ascending=False)
)

highest_source = source_totals.idxmax()

peak_count = int(analysis_df["peak_consumption"].sum())
non_peak_count = len(analysis_df) - peak_count

# SUMMARY CARDS
st.markdown(
    '<div class="section-heading">Consumption Summary</div>',
    unsafe_allow_html=True
)

c1, c2, c3, c4 = st.columns(4)

metrics = [
    (c1, "⚡", "Total Usage", f"{total:,.2f} kWh"),
    (c2, "📊", "Average Usage", f"{average:,.2f} kWh"),
    (c3, "⬆️", "Maximum Usage", f"{maximum:,.2f} kWh"),
    (c4, "🔋", "Leading Source", highest_source)
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

# DAILY TREND
st.markdown(
    '<div class="section-heading">Daily Consumption Trend</div>',
    unsafe_allow_html=True
)

daily_data = (
    analysis_df.groupby(
        analysis_df["timestamp"].dt.date
    )["consumption_kwh"]
    .sum()
    .reset_index()
)

daily_data.columns = ["Date", "Consumption"]

st.caption("Total recorded electricity usage for each day.")

st.line_chart(
    daily_data.set_index("Date"),
    y="Consumption",
    x_label="Date",
    y_label="Energy (kWh)"
)

# ENERGY SOURCE ANALYSIS
st.markdown(
    '<div class="section-heading">Energy Source Performance</div>',
    unsafe_allow_html=True
)

left, right = st.columns(2)

with left:
    st.markdown("#### Source-wise Consumption")

    st.bar_chart(
        source_totals,
        horizontal=True,
        x_label="Energy (kWh)"
    )

with right:
    st.markdown("#### Source Distribution")

    fig, ax = plt.subplots(figsize=(5, 4))

    ax.pie(
        source_totals,
        labels=source_totals.index,
        autopct="%1.1f%%",
        startangle=90
    )

    ax.set_title("Consumption Share by Source")
    st.pyplot(fig)
    plt.close(fig)

# PEAK CONSUMPTION ANALYSIS
st.markdown(
    '<div class="section-heading">Peak Consumption Analysis</div>',
    unsafe_allow_html=True
)

p1, p2 = st.columns(2)

with p1:
    st.metric("Peak Records", peak_count)

with p2:
    st.metric("Non-Peak Records", non_peak_count)

peak_data = pd.Series({
    "Peak": peak_count,
    "Non-Peak": non_peak_count
})

st.bar_chart(
    peak_data,
    horizontal=True
)

# HIGHEST CONSUMPTION RECORD
st.markdown(
    '<div class="section-heading">Highest Consumption Record</div>',
    unsafe_allow_html=True
)

st.info(
    f"The highest recorded consumption is "
    f"{maximum:,.2f} kWh on "
    f"{highest_record['timestamp'].strftime('%d %b %Y')}."
)

# ANALYSIS INSIGHTS
st.markdown(
    '<div class="section-heading">🔍 Analysis Insights</div>',
    unsafe_allow_html=True
)

st.write(
    f"• {highest_source} is the largest recorded energy source "
    f"with {source_totals.max():,.2f} kWh."
)

st.write(
    f"• Average consumption per record is {average:,.2f} kWh."
)

st.write(
    f"• {peak_count} records are marked as peak consumption."
)

st.write(
    f"• The minimum recorded consumption is {minimum:,.2f} kWh."
)

# DETAILED DATA
with st.expander("View Detailed Analysis Data"):
    st.dataframe(
        analysis_df,
        use_container_width=True,
        hide_index=True
    )

# DOWNLOAD ANALYSIS
csv_data = analysis_df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Download Analysis Data",
    data=csv_data,
    file_name="energy_analysis.csv",
    mime="text/csv"
)

# FOOTER
st.markdown(
    '<div class="footer">ENERGY SAVER | Energy Analysis</div>',
    unsafe_allow_html=True
)