import threading
import time
from src.budget import Budget
from functools import wraps
from datetime import datetime
import logging

logging.basicConfig(filename='notifier.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def log_action(func):
    """Decorator to log actions in the Notifier class."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        # log the method name and the current time
        logging.info(f"Calling {func.__name__}...")
        result = func(*args, **kwargs)
        logging.info(f"Finished {func.__name__}.")
        return result
    return wrapper

class Notifier:
    
    def __init__(self, budget: Budget, interval: int = 60):
        """Initializes the notifier with a budget and check interval in seconds."""
        self.budget = budget
        self.interval = interval 
        self.running = False
        self.thread = None
        
    
    @log_action
    def start(self):
        """Starts the notifier in a background thread."""  
        if not self.running:
            self.running = True
            self.thread = threading.Thread(target=self._run, daemon=True)
            self.thread.start()
            print("Notifier started")
    
    
    @log_action        
    def stop(self):
        """Stops the notifier."""
        if not self.running:
            print("Notifier is not running")
            return 
        self.running = False
        self.thread.join()
        print("Notifier stopped")
            
    
    
    @log_action
    def _run(self):
        """Continuously checks budget limits at the set interval."""
        while self.running:
            warnings = self.budget.check_limits()
            if warnings:
                print("\n".join(warnings))
            time.sleep(self.interval)