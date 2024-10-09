# RSS News Categorization

## Overview
RSS News Categorization is a project that leverages Natural Language Processing (NLP) techniques to categorize news articles from various RSS feeds. The objective is to automatically classify news articles into predefined categories, making it easier for users to navigate through the information.

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Contact](#contact)

## Features
- Fetches news articles from multiple RSS feeds.
- Categorizes articles into predefined categories (e.g., Politics, Sports, Technology).
- Option to filter articles by category.
- Real-time updates for new articles.

## Technologies Used
- Python
- feedparser (for parsing RSS feeds)
- Hugging Face Transformers (for categorization using transformer models)
- Pandas (for data manipulation)
- NLTK/Spacy (for NLP tasks)
- PostgreSQL (for database management)
- Redis (for caching)
- Celery (for asynchronous task management)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/harshikagoyal14/rss_news_categorization.git

2. Navigate to the project directory:
   ```bash
   cd rss_news_categorization
3. Create a virtual environment
   ```bash
   python -m venv venv
4. Install the required packages:
   ```bash
   pip install -r requirements.txt


##Usage 
1. Configure the Database:
   
Add your PostgreSQL database connection details in config.py.

2. Start Redis: Make sure Redis is running. You can start Redis with
   ```bash
   redis-server
3. Start Celery Workers:

   1. Open a new terminal and navigate to the project directory.
   2. Start the Celery worker:
      ```bash
      celery -A your_celery_app worker --loglevel=info
     (Replace your_celery_app with your actual Celery application name.)
4. Start Celery Beat:
      ```bash
      celery -A your_celery_app beat --loglevel=info

5. Run the application:
   ```bash
   python app.py
6. Fetch the Results:
   For fetching the results open an interactive python  environment and run:
   ```bash
   from your_module import fetch_all_feeds
   fetch_all_feeds()
The application will fetch news articles, categorize them, and you can monitor the results in the app.log file.


## Contact 
1. Name: Harshika Goyal
2. Email: goyalharshika266@gmail.com
   
