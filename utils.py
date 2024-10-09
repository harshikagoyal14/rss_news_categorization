# utils.py
import csv
from models import session, NewsArticle
from logging_setup import log_event, log_error

def export_to_csv():
    try:
        articles = session.query(NewsArticle).all()
        with open('data/news_articles.csv', mode='w') as file:
            writer = csv.writer(file)
            writer.writerow(['ID', 'Title', 'Content', 'Publication Date', 'URL', 'Source', 'Category'])
            for article in articles:
                writer.writerow([article.id, article.title, article.content, article.pub_date, article.url, article.source, article.category])
        log_event("Data exported to CSV")
    except Exception as e:
        log_error(f"Error exporting data to CSV: {str(e)}")
