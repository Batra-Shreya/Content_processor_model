import os
from dotenv import load_dotenv
load_dotenv()
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = os.getenv("MONGO_URI")

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client["content_processor_db"]
articles_collection = db["articles"]

def store_article(article):
    # Check for duplicate based on URL
    if articles_collection.find_one({"url": article["url"]}):
        return "Already exists"

    result = articles_collection.insert_one(article)
    return result.inserted_id

def article_exists(url):
    if articles_collection.find_one({"url": url}):
        return True
    else:
        return False
