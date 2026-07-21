import os
import logging
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from src.utils import setup_logging

load_dotenv()
setup_logging()

def get_database_engine():
    """Creates and returns a SQLAlchemy engine connected to Neon Postgres."""
    db_url = os.getenv("DATABASE_URL")
    if not db_url:
        logging.error("DATABASE_URL is missing from environment variables!")
        return None
    try:
        engine = create_engine(db_url)
        return engine
    except Exception as e:
        logging.error(f"Failed to create database engine: {e}")
        return None

def test_connection():
    """Tests the connection to the cloud database."""
    engine = get_database_engine()
    if not engine:
        return False
    
    try:
        with engine.connect() as connection:
            result = connection.execute(text("SELECT version();"))
            for row in result:
                logging.info(f"Successfully connected to Neon PostgreSQL! Version: {row[0]}")
        return True
    except Exception as e:
        logging.error(f"Connection test failed: {e}")
        return False

def load_dataframe_to_postgres(df, table_name="crypto_prices"):
    """Loads a cleaned pandas DataFrame directly into PostgreSQL."""
    if df.empty:
        logging.warning("DataFrame is empty. Nothing to load.")
        return

    engine = get_database_engine()
    if not engine:
        return

    try:
        # Pandas to_sql handles table creation and appending automatically
        df.to_sql(
            name=table_name,
            con=engine,
            if_exists='append',  # Keeps historical time-series data
            index=False
        )
        logging.info(f"Successfully loaded {len(df)} rows into Neon table '{table_name}'!")
    except Exception as e:
        logging.error(f"Error loading data to PostgreSQL: {e}")

if __name__ == "__main__":
    # Test the connection when running load.py directly
    test_connection()