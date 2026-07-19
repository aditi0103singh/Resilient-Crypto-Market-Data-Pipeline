import os
import requests
from dotenv import load_dotenv

# Load the secret from .env file
load_dotenv()
api_key = os.getenv('CG_API_KEY')

def fetch_crypto_price():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
    
    # Use the correct header for CoinGecko
    headers = {
        "x-cg-demo-api-key": api_key,
        "accept": "application/json"
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status() # This triggers the error if the status is 4xx or 5xx
        data = response.json()
        print(f"Success! Data: {data}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")

if __name__ == "__main__":
    fetch_crypto_price()