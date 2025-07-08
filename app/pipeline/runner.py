from ingestion.news_fetch import fetch_news
from processing.summarizer import summarize_news
from db.mongo import store_article, article_exists
import logging


def ingest_news(language="en", page=1):
    logging.warning("Inside the runner")
    articles = fetch_news(language=language, page=page)
    articles= articles[:2]
    logging.warning(f"got {len(articles)} from the api")
    new_articles = []

    for article in articles:
        if not article.get("url"):
            continue
        if article_exists(article["url"]):
            continue
        new_articles.append(article)

    logging.warning(f"Summarizing {len(new_articles)} new articles")
    summarized_articles = summarize_news(new_articles)
    for article in summarized_articles:
        store_article(article)
    return summarized_articles

def search_news(query):
    logging.warning("Inside the search news")
    results = search_news(query)
    return results