import os
import requests
import time
import logging
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from dotenv import load_dotenv

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
        return response.json()
    except Exception as e:
        logging.error(f"Extraction failed: {e}")
        return None