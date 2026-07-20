import os
import time
import logging
from dotenv import load_dotenv
from src.extract import fetch_crypto_data
from src.transform import clean_batch

load_dotenv()
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def run_pipeline(num_requests):
    api_key = os.getenv('CG_API_KEY')
    output_file = "data/cleaned/master_data.csv"
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    
    # Check if file exists to decide whether to write the header
    file_exists = os.path.isfile(output_file)

    for i in range(num_requests):
        logging.info(f"Processing request {i+1}/{num_requests}")
        
        data = fetch_crypto_data(api_key)
        
        if data:
            df = clean_batch(data)
            
            if not df.empty:
                # If file doesn't exist, write header. If it does, don't.
                df.to_csv(output_file, mode='a', header=not file_exists, index=False)
                
                # After the first run, ensure file_exists is True so headers aren't added again
                file_exists = True
                logging.info(f"Request {i+1} saved with timestamp.")
        
        time.sleep(1.2)

if __name__ == "__main__":
    run_pipeline(20) # Change this to 1000 whenever you are ready!