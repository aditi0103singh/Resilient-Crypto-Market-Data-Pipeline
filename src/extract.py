import os
import requests
import time
import logging
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from dotenv import load_dotenv

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

load_dotenv()

# Create a persistent session
session = requests.Session()
retries = Retry(total=5, backoff_factor=1, status_forcelist=[429, 500, 502, 503, 504])
session.mount("https://", HTTPAdapter(max_retries=retries))

def fetch_crypto_data(api_key=None, coin_ids="bitcoin,ethereum,solana"):
    # If api_key is not passed, automatically grab it from environment variables
    if not api_key:
        api_key = os.getenv("COINGECKO_API_KEY")

    url = "https://api.coingecko.com/api/v3/simple/price"
    headers = {"x-cg-demo-api-key": api_key} if api_key else {}
    params = {"ids": coin_ids, "vs_currencies": "usd"}
    
    try:
        response = session.get(url, headers=headers, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        # --- DAY 6: DEFENSIVE PROGRAMMING CHECK ---
        if not data:
            logging.warning("Warning: Received an empty payload from the CoinGecko API.")
            return None
            
        return data

    except Exception as e:
        logging.error(f"Extraction failed: {e}")
        return None

if __name__ == "__main__":
    logging.info("Starting crypto data extraction...")
    crypto_data = fetch_crypto_data()
    if crypto_data:
        logging.info(f"Successfully fetched data: {crypto_data}")
    else:
        logging.warning("No data returned or extraction failed.")