from fastapi import FastAPI
from pipeline.runner import ingest_news
import logging

app = FastAPI()

@app.get("/")
def root():
    return {"message":"api is working!"}

@app.post("/ingest_news")
def ingest_news_route():
    logging.warning("Started ingest news api")
    results = ingest_news()
    return {"inserted": len(results)}

@app.post("/search_news")
def search_news_route():
    logging.warning("Started search news api")
    results = search_news()
    return {"results": results}
