from sqlalchemy import Column, Integer, String, DateTime, Text, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import DATABASE_URL

Base = declarative_base()

class NewsArticle(Base):
    __tablename__ = 'news_articles'

    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    content = Column(Text)
    publication_date = Column(DateTime)
    source_url = Column(String(500))  # Ensure this is defined
    category = Column(String(100))
    pub_date = Column(DateTime)
    source = Column(String(100))  # Add this line to define the source

# Database setup
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

def init_db():
    Base.metadata.create_all(engine)  # Ensure the database tables are created
