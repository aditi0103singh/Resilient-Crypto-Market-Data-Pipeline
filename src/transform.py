import pandas as pd
from datetime import datetime

def clean_batch(raw_data):
    # Flatten the nested structure (e.g., {'bitcoin': {'usd': 64000}})
    # If raw_data is a dictionary, orient='index' works perfectly
    df = pd.DataFrame.from_dict(raw_data, orient='index').reset_index()
    
    # Rename columns
    df.columns = ['crypto_id', 'price_usd']
    
    # Add execution timestamp (The "Idempotency" key)
    df['execution_time'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Clean up types
    df['price_usd'] = pd.to_numeric(df['price_usd'], errors='coerce')
    df = df.dropna(subset=['price_usd'])
    
    return df