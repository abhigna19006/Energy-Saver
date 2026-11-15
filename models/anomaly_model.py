from sklearn.ensemble import IsolationForest

def detect_anomalies(data):

    features = ["Fan", "Lights", "AC", "Other"]

    model = IsolationForest(
        contamination=0.10,
        random_state=42
    )

    predictions = model.fit_predict(data[features])

    results = data.copy()

    results["Detection"] = predictions

    results["Status"] = results["Detection"].map({
        1: "Normal",
        -1: "Unusual Usage"
    })

    return results