
import sys
import os

# Add the parent directory of src to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import logging
import time
from src.budget import Budget
from datetime import datetime
import argparse


# Configure logging
logging.basicConfig(
    filename='notifier.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def run_notifier(user_id: str, interval: int):
    """
    Main function to run the notifier.
    
    Args:
        user_id (str): The user ID for which to check the budget.
        interval (int): Time in seconds between budget checks.
    """
    
    budget = Budget(user_id)
    print(f"Notifier started for user '{user_id}' with intervals - {interval}")
    
    try:
        while True:
            warnings = budget.check_limits()
            if warnings:
                for warning in warnings:
                    
                    print(warning, flush=True)
                    logging.warning(warning)
                # print(f"[{datetime.now()}] Budget warnings:")
                # print("\n".join(Warnings), flush=True)
            time.sleep(interval)
            
    except KeyboardInterrupt:
        print(f"Notifier for user: {user_id} stopped")
        exit(0)
        

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description="Run the budget notifier.")
    parser.add_argument("--user_id", required=True, help="User ID for the notifier.")
    parser.add_argument("--interval", type=int, default=60, help="Interval (in seconds) for checking limits.")
    args = parser.parse_args()

    run_notifier(user_id=args.user_id, interval=args.interval)
    
    