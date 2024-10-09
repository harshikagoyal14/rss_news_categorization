

from tasks import app, fetch_and_process
from logging_setup import log_event
from models import init_db
from feed_parser import fetch_all_feeds

@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Schedule the periodic task to run every 5 minutes
    sender.add_periodic_task(300.0, fetch_and_process.s(), name='Fetch and process articles every 5 minutes')

if __name__ == "__main__":
    # Initialize the database
    init_db()
    log_event("Database initialized")
    fetch_all_feeds()  
    
    print("App initialized. Now start Celery worker and beat using separate commands.")
