import os
import pandas as pd
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

def load_crypto_data(df: pd.DataFrame, table_name: str = "crypto_prices"):
    if df.empty:
        print("DataFrame is empty. Nothing to load.")
        return

    try:
        engine = create_engine(DATABASE_URL)
        
        with engine.begin() as connection:
            success_count = 0
            for _, row in df.iterrows():
                # Constructing an UPSERT query for PostgreSQL
                # Assumes 'symbol' is your unique constraint/primary key column
                query = text(f"""
                    INSERT INTO {table_name} (symbol, price, timestamp)
                    VALUES (:symbol, :price, :timestamp)
                    ON CONFLICT (symbol) 
                    DO UPDATE SET 
                        price = EXCLUDED.price,
                        timestamp = EXCLUDED.timestamp;
                """)
                
                connection.execute(query, {
                    "symbol": row.get("symbol"),
                    "price": row.get("price"),
                    "timestamp": row.get("timestamp")
                })
                success_count += 1
                
        print(f"Successfully upserted {success_count} rows into '{table_name}'.")
        
    except Exception as e:
        print(f"Error loading data into database: {e}")