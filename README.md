# Flight Delay Data Drift Report

## 📌 Project Description

This project focuses on analyzing **data drift** in the `DelayedFlights.csv` dataset, available on Kaggle:  
👉 [Airline Delay Causes Dataset](https://www.kaggle.com/datasets/giovamata/airlinedelaycauses)

The analysis is performed using the **Evidently AI** library.

---

## 🧪 Project Steps

1. **Load and clean** the `DelayedFlights.csv` dataset  
2. **Select relevant features**: arrival delays, departure delays, and specific delay causes  
3. **Simulate two datasets**: reference and current  
4. **Generate a data drift report** using `Evidently`  
5. **Export the report** as an HTML file: `delayed_flights_drift_report.html`

---

## 📊 Analyzed Features

- `ArrDelay`  
- `DepDelay`  
- `CarrierDelay`  
- `WeatherDelay`  
- `NASDelay`  
- `SecurityDelay`  
- `LateAircraftDelay`

---

## 📈 Tool Used

- **Evidently AI** – An open-source library for monitoring data and machine learning model quality.

---
