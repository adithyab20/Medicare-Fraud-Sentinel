import pandas as pd
import requests
import os

def download_medicare_sample(limit=1000):
    """
    Downloads a sample of Medicare Physician data from CMS.gov
    """
    # CMS Data API URL for Physician & Other Practitioners (2022/2023 data)
    api_url = "https://data.cms.gov/provider-data/api/1.0/dataset/8672-03e5/download"
    
    print(f"--- Starting download from CMS ---")
    
    # In a real scenario, we'd stream this. For a sample, we use pandas.
    # Note: CMS links often trigger a direct CSV download
    try:
        # Saving locally to our 'data/raw' folder
        output_path = 'data/raw/medicare_sample.csv'
        
        # Create directory if it doesn't exist
        os.makedirs('data/raw', exist_ok=True)
        
        # Download the file
        response = requests.get(api_url)
        with open(output_path, 'wb') as f:
            f.write(response.content)
            
        print(f"--- Success! Data saved to {output_path} ---")
        
        # Show a preview
        df = pd.read_csv(output_path, nrows=5)
        print("\nData Preview:")
        print(df.head())
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    download_medicare_sample()