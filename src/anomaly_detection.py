import pandas as pd
from sklearn.ensemble import IsolationForest
import os

def detect_billing_anomalies():

    file_path = 'data/raw/medicare_advantage_data.xlsx'
    
    if not os.path.exists(file_path):
        print(" File not found. Please ensure the Excel file is in data/raw/")
        return

    # Load Table 3 (Area of Residence) which we identified in the notebook
    df = pd.read_excel(file_path, sheet_name=3, skiprows=3)
    
    # Cleaning: Remove empty rows and summary 'Totals'
    df = df.dropna(subset=['Area of Residence'])
    df = df[~df['Area of Residence'].str.contains("Total|Residence", na=False)]
    
    # Feature Selection: We'll use 'Services' and 'Payments' per enrollee
    col_services = [c for c in df.columns if 'Services Per Original' in c][0]
    col_payments = [c for c in df.columns if 'Program Payments Per Original' in c][0]
    
    X = df[[col_services, col_payments]].fillna(0)

    # --- Isolation Forest Model ---
    model = IsolationForest(contamination=0.1, random_state=42) 
    df['anomaly_score'] = model.fit_predict(X)
    
    anomalies = df[df['anomaly_score'] == -1]

    print(f"🔍 Fraud Sentinel found {len(anomalies)} regional anomalies.")
    print("\n--- Top Flagged Anomalous Regions ---")
    # Display the regions flagged by the algorithm
    print(anomalies[['Area of Residence', col_payments]].sort_values(by=col_payments, ascending=False).head())

if __name__ == "__main__":
    detect_billing_anomalies()