import os
import pandas as pd
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

load_dotenv()

def get_database_engine():
    database_url = os.getenv("DATABASE_URL")
    if not database_url:
        raise ValueError("DATABASE_URL environment variable is not set!")
    return create_engine(database_url)

def load_crypto_data(df: pd.DataFrame, table_name: str = "crypto_prices"):
    """
    Takes a pandas DataFrame and loads it into the PostgreSQL database using an upsert.
    Expected DataFrame columns: symbol, price, timestamp
    """
    engine = get_database_engine()
    
    print(f"Loading {len(df)} rows into database table '{table_name}'...")
    
    # Ensure columns match what the SQL expects
    required_columns = ["symbol", "price", "timestamp"]
    for col in required_columns:
        if col not in df.columns:
            raise ValueError(f"Missing required column in DataFrame: '{col}'. Found columns: {list(df.columns)}")

    try:
        with engine.begin() as connection:
            for _, row in df.iterrows():
                # Clean or map values safely
                symbol_val = str(row["symbol"]).strip().upper()
                price_val = float(row["price"]) if pd.notnull(row["price"]) else 0.0
                timestamp_val = row["timestamp"]

                sql_query = text(f"""
                    INSERT INTO {table_name} (symbol, price, timestamp)
                    VALUES (:symbol, :price, :timestamp)
                    ON CONFLICT (symbol) 
                    DO UPDATE SET 
                        price = EXCLUDED.price,
                        timestamp = EXCLUDED.timestamp;
                """)
                
                connection.execute(
                    sql_query, 
                    {
                        "symbol": symbol_val, 
                        "price": price_val, 
                        "timestamp": timestamp_val
                    }
                )
        print("Data loaded successfully into the database!")
        
    except Exception as e:
        print(f"Error loading data into database: {e}")
        raise e