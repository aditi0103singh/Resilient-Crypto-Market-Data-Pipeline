from src.extract import fetch_crypto_data
from src.transform import clean_batch
from src.load import load_crypto_data  # <--- Import your new load function

def run_pipeline():
    print("Starting Crypto ETL Pipeline...")
    
    # 1. Extract
    raw_data = fetch_crypto_data()
    
    # 2. Transform
    cleaned_df = clean_batch(raw_data)
    
    # 3. Load (New Step!)
    if not cleaned_df.empty:
        load_crypto_data(cleaned_df, table_name="crypto_prices")
    else:
        print("Pipeline halted: No data to load.")
        
    print("Pipeline finished!")

if __name__ == "__main__":
    run_pipeline()