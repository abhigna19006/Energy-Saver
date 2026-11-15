⚡ Energy Saver – Smart Energy Consumption Monitoring

Power Smarter. Live Greener.

📌 Project Overview

Energy Saver is a Python-based web application designed to monitor electricity consumption, analyse energy usage patterns, identify unusual consumption readings using machine learning, and provide personalized energy-saving recommendations.

The application uses a cleaned electricity consumption dataset containing 500 records.

🎯 Problem Statement

Electricity wastage and inefficient energy consumption can increase electricity bills and affect energy sustainability. Users need a simple system to understand their consumption patterns and identify unusual usage.

Energy Saver helps users analyse their electricity consumption and make informed energy-saving decisions.

🎯 Project Objectives

- Monitor electricity consumption.
- Analyse energy usage patterns.
- Identify unusual consumption readings using AI.
- Provide energy-saving recommendations.
- Help users understand energy consumption through interactive visualizations.
- Estimate possible electricity bill savings.

✨ Key Features

1. Energy Dashboard

- Displays total and average energy consumption.
- Shows peak consumption percentage.
- Provides energy source analysis.
- Displays consumption trends using charts.

2. Energy Analysis

- Analyses electricity consumption records.
- Displays daily consumption trends.
- Compares Grid, Solar and Battery consumption.
- Provides detailed consumption reports.

3. AI-Based Unusual Usage Detection

- Uses the Isolation Forest machine learning algorithm.
- Identifies unusual energy consumption readings.
- Displays normal and unusual readings.
- Provides downloadable AI detection results.

4. Energy Saver Bot

- Provides information about electricity conservation.
- Answers predefined energy-saving questions.
- Suggests ways to reduce electricity bills.

5. Smart Recommendations

- Analyses energy source consumption.
- Provides energy-saving suggestions.
- Allows users to enter estimated appliance consumption.
- Calculates possible savings based on user-selected targets.

6. About Project

- Explains the project overview, objectives, workflow, technologies and scope.

🛠️ Technologies Used

Technology| Purpose
Python| Application development
Streamlit| Web application interface
Pandas| Data processing and analysis
Matplotlib| Data visualization
Scikit-learn| Machine learning and anomaly detection
HTML| Web content structure
CSS| Application styling
Excel| Energy consumption dataset

📊 Dataset Information

The application uses a cleaned Excel dataset containing 500 electricity consumption records.

Important dataset columns:

- "facility_id"
- "timestamp"
- "consumption_kwh"
- "consumption_source"
- "peak_consumption"

Energy sources include:

- Grid
- Solar
- Battery

The dataset is stored in the "data" folder as "energy_data.xlsx".

Note: The dataset does not contain individual appliance-level readings. Appliance consumption entered in the Recommendations page is treated as an estimate.

🤖 Machine Learning Algorithm

Isolation Forest

Isolation Forest is an unsupervised machine learning algorithm used to identify unusual data patterns.

In this project, it analyses electricity consumption readings and identifies unusual readings for further investigation.

An unusual reading does not automatically prove electricity wastage, appliance faults or electricity theft.

📁 Project Structure

Energy-Saver/
│
├── app.py
├── requirements.txt
├── README.md
│
├── styles/
│   └── style.css
│
├── data/
│   └── energy_data.xlsx
│
├── pages/
│   ├── 1_Dashboard.py
│   ├── 2_Energy_Analysis.py
│   ├── 3_AI_Detection.py
│   ├── 4_Energy_Bot.py
│   ├── 5_Recommendations.py
│   └── 6_About_Project.py
│
├── models/
│   └── anomaly_model.py
│
└── utils/
    ├── calculations.py
    └── data_loader.py

⚙️ Installation and Execution

Step 1: Install Python

Install Python on your system.

Step 2: Open the project folder

Open the Energy-Saver folder in VS Code.

Step 3: Create a virtual environment

python -m venv .venv

Step 4: Activate the virtual environment (Windows PowerShell)

.venv\Scripts\Activate.ps1

Step 5: Install required packages

python -m pip install -r requirements.txt

Step 6: Run the application

python -m streamlit run app.py

The Energy Saver application will open in your web browser.

🌱 Current Project Scope

This version uses a cleaned electricity consumption dataset containing 500 records. It analyses energy consumption, identifies unusual usage patterns and provides energy-saving recommendations.

AI detection results are intended for further investigation. The application does not directly control electrical appliances or automatically prevent electricity wastage.

🔮 Future Enhancements

- Real-time electricity monitoring.
- IoT-based smart meter integration.
- Appliance-level energy tracking.
- Advanced AI-based consumption forecasting.
- Automated energy-saving alerts.

🏁 Conclusion

Energy Saver provides a simple and interactive platform for monitoring and analysing electricity consumption. By combining data analysis, machine learning and personalized recommendations, the project encourages smarter electricity usage and energy conservation.

Power Smarter. Live Greener. ⚡