import pandas as pd
import numpy as np
from evidently import ColumnMapping
from evidently import *
from evidently import Report
from evidently.legacy.metrics import DatasetDriftMetric, DataDriftTable
from evidently.legacy.pipeline.column_mapping import ColumnMapping
from evidently import Report
from evidently.legacy.metric_preset import ClassificationPreset, RegressionPreset
from evidently.metrics import *

# Path to the dataset
dataset_path = "DelayedFlights.csv"  # Adjust this path if needed

# Load the dataset
df = pd.read_csv(dataset_path)

print("Dataset loaded successfully. First few rows:")
print(df.head())

# Split data into reference and current datasets
total_rows = len(df)
reference_data = df.iloc[:total_rows//2]  # First half as reference
current_data = df.iloc[total_rows//2:]    # Second half as current

print(f"\nReference data shape: {reference_data.shape}")
print(f"Current data shape: {current_data.shape}")

# Selecting columns for analysis
columns_to_analyze = [
    'ArrDelay', 'DepDelay', 'CarrierDelay', 'WeatherDelay',
    'NASDelay', 'SecurityDelay', 'LateAircraftDelay',
    'UniqueCarrier', 'Origin', 'Dest'
]

reference_subset = reference_data[columns_to_analyze]
current_subset = current_data[columns_to_analyze]

# Define column mapping for numeric and categorical features
column_mapping = ColumnMapping()
column_mapping.numerical_features = [
    'ArrDelay', 'DepDelay', 'CarrierDelay', 'WeatherDelay',
    'NASDelay', 'SecurityDelay', 'LateAircraftDelay'
]
column_mapping.categorical_features = ['UniqueCarrier', 'Origin', 'Dest']

# Create the drift report with the updated metrics
drift_report = Report(
    metrics=[
        DatasetDriftMetric(),
        DataDriftTable()
    ]
)

# Run the report
drift_report.run(
    reference_data=reference_subset,
    current_data=current_subset,
    column_mapping=column_mapping
)

# Save the report
drift_report.save_html("flight_data_drift_report.html")
print("\nData drift report generated and saved as 'flight_data_drift_report.html'.")

print("\nNext steps for submission:")
print("1. Open 'flight_data_drift_report.html' to analyze the results and write your findings.")
print("2. Create a GitHub repository (e.g., 'FlightDelayAnalysis').")
print("3. Add this script, the report ('flight_data_drift_report.html'), and a README.md with your discussion.")
print("4. Push to GitHub and submit the repository URL.")