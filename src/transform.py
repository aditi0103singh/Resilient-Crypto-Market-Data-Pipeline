import pandas as pd
from datetime import datetime

def clean_batch(raw_data):
    if not raw_data:
        return pd.DataFrame()
        
    rows = []
    current_time = datetime.utcnow()
    
    for coin_id, data in raw_data.items():
        rows.append({
            "symbol": coin_id.upper(),          # Must match 'symbol'
            "price": data.get("usd"),           # Must match 'price'
            "timestamp": current_time           # Must match 'timestamp'
        })
        
    return pd.DataFrame(rows)