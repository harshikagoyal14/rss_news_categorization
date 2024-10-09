import sys
from pathlib import Path
from celery import Celery

# Add the current directory to the Python path
sys.path.append(str(Path(__file__).resolve().parent))

# Initialize the Celery app
app = Celery('tasks', broker='redis://localhost:6379/0')

app.conf.broker_connection_retry_on_startup = True

@app.task
def fetch_and_process():
    try:
        from logging_setup import log_event, log_error  # Import logging functions here
        from feed_parser import fetch_all_feeds  # Import feed fetching here

        log_event("Starting to fetch and process articles...")
        
        fetch_all_feeds()  # Call the function to fetch feeds

        log_event("Fetched and processed articles successfully.")
    except Exception as e:
        log_error(f"Error fetching and processing articles: {str(e)}")
