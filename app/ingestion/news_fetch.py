from newsapi import NewsApiClient
import os
from dotenv import load_dotenv
import logging
from newspaper import Article
load_dotenv()  
news_api_key = os.getenv("NEWS_API_KEY")

country_news = os.getenv("COUNTRY")
newsapi = NewsApiClient(api_key=news_api_key)

def fetch_news(language, page):   
    # all_articles = newsapi.get_everything(q=query,
    #                                     sources=sources,
    #                                     domains=domains,
    #                                     from_param=from_date,
    #                                     to=to_date,
    #                                     language=language,
    #                                     sort_by='relevancy',
    #                                     page=2)
    logging.warning(f"Fetching news for {language} and page {page}")
    top_headlines = newsapi.get_top_headlines(
    language=language,
    page=page,
    page_size=20,  # max 100 if needed
    country=country_news   # optional, but helps focus
)


    return top_headlines['articles']


def fetch_full_article(url):
    try:
        article = Article(url)
        article.download()
        article.parse()
        return article.text
    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return None





