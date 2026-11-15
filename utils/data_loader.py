from pathlib import Path
import pandas as pd

DATA_PATH = (
    Path(__file__).resolve().parents[1]
    / "data"
    / "energy_data.xlsx"
)

def load_energy_data():
    df = pd.read_excel(DATA_PATH)

    required_columns = [
        "facility_id",
        "timestamp",
        "consumption_kwh",
        "consumption_source",
        "peak_consumption",
    ]

    df = df[required_columns].copy()

    df["timestamp"] = pd.to_datetime(
        df["timestamp"], errors="coerce"
    )

    df["consumption_kwh"] = pd.to_numeric(
        df["consumption_kwh"], errors="coerce"
    )

    df = df.dropna(
        subset=["timestamp", "consumption_kwh"]
    )

    return df