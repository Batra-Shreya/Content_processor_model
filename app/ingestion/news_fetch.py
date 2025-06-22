from newsapi import NewsApiClient
import os
from dotenv import load_dotenv

load_dotenv()  
news_api_key = os.getenv("NEWS_API_KEY")


newsapi = NewsApiClient(api_key=news_api_key)

def fetch_news(query, from_date, to_date, sources, domains, language, sort_by, page):   
    all_articles = newsapi.get_everything(q=query,
                                        sources=sources,
                                        domains=domains,
                                        from_param=from_date,
                                        to=to_date,
                                        language=language,
                                        sort_by='relevancy',
                                        page=2)

    return all_articles







