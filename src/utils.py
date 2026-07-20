import logging
import os

# Centralized Configuration
RAW_DATA_PATH = "data/raw/"
CLEAN_DATA_PATH = "data/cleaned/master_data.csv"
API_URL = "https://api.coingecko.com/api/v3/simple/price"

def setup_logging():
    """Sets up standard logging for all modules."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler("pipeline.log"), # Saves logs to a file
            logging.StreamHandler()              # Prints logs to the console
        ]
    )

def ensure_directories():
    """Ensures data folders exist so the code doesn't crash."""
    os.makedirs(RAW_DATA_PATH, exist_ok=True)
    os.makedirs(os.path.dirname(CLEAN_DATA_PATH), exist_ok=True)