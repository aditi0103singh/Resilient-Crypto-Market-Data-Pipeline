import logging
from src.utils import setup_logging
from src.extract import fetch_crypto_data
from src.transform import clean_batch as clean_crypto_data
from src.load import load_dataframe_to_postgres

def run_pipeline():
    # 1. Setup logging
    setup_logging()
    logging.info("--- Starting Crypto ETL Pipeline ---")

    # 2. EXTRACT
    logging.info("Phase 1: Extracting data from API...")
    raw_data = fetch_crypto_data()
    
    if not raw_data:
        logging.error("Extraction failed. Aborting pipeline.")
        return

    # 3. TRANSFORM
    logging.info("Phase 2: Transforming and cleaning data...")
    df = clean_crypto_data(raw_data)
    
    if df.empty:
        logging.error("Transformation resulted in empty data. Aborting pipeline.")
        return

    # 4. LOAD (Now pushing straight to Neon Cloud DB!)
    logging.info("Phase 3: Loading data into Neon PostgreSQL...")
    load_dataframe_to_postgres(df, table_name="crypto_prices")

    logging.info("--- Pipeline Completed Successfully! ---")

if __name__ == "__main__":
    run_pipeline()