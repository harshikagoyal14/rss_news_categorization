import feedparser  # Ensure this is correctly imported
from models import NewsArticle, session
from config import RSS_FEEDS
import datetime
from logging_setup import log_event, log_error
from categorize import categorize_article
from urllib.parse import urlparse

def normalize_url(url):
    """Normalizes the URL."""
    parsed_url = urlparse(url)
    return f"{parsed_url.scheme}://{parsed_url.netloc}{parsed_url.path}"  # Normalizes the URL

def parse_feed(url):
    """Parses the RSS feed and adds articles to the database."""
    try:
        feed = feedparser.parse(url)
        log_event(f"Parsing feed: {url}")  # Log which feed is being parsed
        
        for entry in feed.entries:
            title = entry.title
            content = entry.get('summary', 'No content available')
            pub_date = entry.published_parsed if 'published_parsed' in entry else None
            source_url = entry.link
            source = feed.feed.title

            if pub_date:
                pub_date = datetime.datetime(*pub_date[:6])

            normalized_url = normalize_url(source_url)
            
            category = categorize_article(content)  # Always categorize the article
            log_event(f"Article '{title}' categorized as {category}")

            article = NewsArticle(
                title=title,
                content=content,
                pub_date=pub_date,
                source_url=normalized_url,
                source=source,
                category=category
            )

            session.add(article)
            session.commit()  # Make sure to commit after adding
            log_event(f"Article added: {title} (Category: {category})")

    except Exception as e:
        log_error(f"Failed to parse feed {url}: {str(e)}")
        session.rollback()  # Rollback on error

def fetch_all_feeds():
    """Fetches articles from all RSS feeds."""
    for feed_url in RSS_FEEDS:
        parse_feed(feed_url)
