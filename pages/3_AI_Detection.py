import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
import sys

from sklearn.ensemble import IsolationForest

# PROJECT PATH
ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT))

from utils.data_loader import load_energy_data

# PAGE CONFIGURATION
st.set_page_config(
    page_title="AI Energy Detection",
    page_icon="🧠",
    layout="wide"
)

# LOAD CSS
css_path = ROOT / "styles" / "style.css"

if css_path.exists():
    st.markdown(
        f"<style>{css_path.read_text(encoding='utf-8')}</style>",
        unsafe_allow_html=True
    )

# LOAD ACTUAL DATASET
st.title("🧠 AI Energy Waste Detection")
st.caption(
    "Machine learning helps identify unusual electricity "
    "consumption patterns using actual dataset records."
)

try:
    data = load_energy_data()
except Exception as e:
    st.error(f"Unable to load the Excel dataset: {e}")
    st.stop()

if data.empty:
    st.warning("No valid energy records are available.")
    st.stop()

data = data.sort_values("timestamp").copy()

# RUN ISOLATION FOREST
st.markdown(
    '<div class="section-heading">AI Detection Overview</div>',
    unsafe_allow_html=True
)

contamination = st.slider(
    "Expected proportion of unusual readings",
    min_value=0.01,
    max_value=0.15,
    value=0.05,
    step=0.01,
    help="This setting controls how many readings the model may flag for review."
)

model = IsolationForest(
    contamination=contamination,
    random_state=42
)

features = data[["consumption_kwh"]]

data["Detection"] = model.fit_predict(features)

data["Status"] = data["Detection"].map({
    1: "Normal",
    -1: "Unusual Usage"
})

normal_count = int((data["Detection"] == 1).sum())
unusual_count = int((data["Detection"] == -1).sum())

# SUMMARY METRICS
c1, c2, c3 = st.columns(3)

metrics = [
    (c1, "📊", "Readings Analysed", str(len(data))),
    (c2, "✅", "Normal Readings", str(normal_count)),
    (c3, "⚠️", "Unusual Readings", str(unusual_count))
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

# HOW AI DETECTION WORKS
st.markdown(
    '<div class="section-heading">How AI Detection Works</div>',
    unsafe_allow_html=True
)

st.write(
    """
    Energy Saver uses the Isolation Forest machine-learning algorithm.
    The model analyses electricity consumption readings and identifies
    values that differ from the overall consumption pattern.

    It separates readings into two categories:
    - Normal Usage: Readings that follow the learned pattern.
    - Unusual Usage: Readings that differ from the learned pattern.
    """
)

st.info(
    "An unusual reading is only a signal for further investigation. "
    "It does not automatically prove electricity wastage, an appliance "
    "fault, or an energy theft."
)

# CONSUMPTION VISUALIZATION
st.markdown(
    '<div class="section-heading">AI Consumption Pattern Detection</div>',
    unsafe_allow_html=True
)

normal_data = data[data["Detection"] == 1]
unusual_data = data[data["Detection"] == -1]

fig, ax = plt.subplots(figsize=(12, 5))

ax.scatter(
    normal_data["timestamp"],
    normal_data["consumption_kwh"],
    color="#20845B",
    label="Normal",
    s=35
)

ax.scatter(
    unusual_data["timestamp"],
    unusual_data["consumption_kwh"],
    color="red",
    label="Unusual",
    s=65,
    marker="X"
)

ax.set_xlabel("Date")
ax.set_ylabel("Consumption (kWh)")
ax.set_title("Isolation Forest - Unusual Consumption Detection")
ax.legend()
ax.grid(alpha=0.2)

plt.xticks(rotation=30)
plt.tight_layout()

st.pyplot(fig)
plt.close(fig)

# UNUSUAL USAGE REPORT
st.markdown(
    '<div class="section-heading">⚠️ Unusual Usage Reports</div>',
    unsafe_allow_html=True
)

if unusual_count > 0:
    st.warning(
        f"The AI model identified {unusual_count} unusual readings "
        "that may need further review."
    )

    st.dataframe(
        data[data["Detection"] == -1][
            [
                "facility_id",
                "timestamp",
                "consumption_kwh",
                "consumption_source",
                "peak_consumption",
                "Status"
            ]
        ],
        use_container_width=True,
        hide_index=True
    )
else:
    st.success("No unusual readings were detected.")

# ALL DETECTION RESULTS
with st.expander("View All AI Detection Results"):
    st.dataframe(
        data[
            [
                "facility_id",
                "timestamp",
                "consumption_kwh",
                "consumption_source",
                "peak_consumption",
                "Status"
            ]
        ],
        use_container_width=True,
        hide_index=True
    )

# DOWNLOAD RESULTS
csv_data = data.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Download AI Detection Results",
    data=csv_data,
    file_name="energy_ai_detection_results.csv",
    mime="text/csv"
)

# FOOTER
st.markdown(
    '<div class="footer">ENERGY SAVER | AI Detection System</div>',
    unsafe_allow_html=True
)