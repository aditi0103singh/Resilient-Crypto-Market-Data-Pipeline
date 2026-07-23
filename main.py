import os
from src.extract import fetch_crypto_data
from src.transform import clean_batch
from src.load import load_crypto_data

def run_pipeline():
    print("Starting Crypto ETL Pipeline...")
    
    # 1. Extract
    # Automatically grabs API key from environment variables if set
    raw_data = fetch_crypto_data()
    
    if not raw_data:
        print("Pipeline halted: Extraction returned no data.")
        return

    # 2. Transform
    cleaned_df = clean_batch(raw_data)
    
    # 3. Load
    if cleaned_df is not None and not cleaned_df.empty:
        load_crypto_data(cleaned_df, table_name="crypto_prices")
    else:
        print("Pipeline halted: No data to load after transformation.")
        
    print("Pipeline finished!")

if __name__ == "__main__":
    run_pipeline()