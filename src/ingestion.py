import pandas as pd
import os

def load_manual_data():
    # Use forward slashes for Windows compatibility in Python
    file_path = 'data/raw/medicare_advantage_data.xlsx'
    
    if os.path.exists(file_path):
        print(f"✅ Found manual download at {file_path}")
        
        try:
            # Use read_excel for .xlsx files
            df = pd.read_excel(file_path, nrows=5) 
            print("\n--- Data Sample Preview ---")
            print(df.head())
            print("\n🚀 Ingestion Phase Complete!")
        except Exception as e:
            print(f"❌ Error reading the file: {e}")
    else:
        print(f"⚠️ File not found at {file_path}")

if __name__ == "__main__":
    load_manual_data()