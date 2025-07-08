indexMapping = {
    "properties":{
        "title":{
            "type":"text",
            "analyzer":"english"
        },
        "content":{
            "type":"text",
            "analyzer":"english"
        },
        "url":{
            "type":"keyword"
        },
        "date":{
            "type":"date"
        },
        "author":{
            "type":"text",
        },
        "summary":{
            "type":"text",
            "analyzer":"english"
        },
        "embedding":{
            "type":"dense_vector",
            "dims":1024,
            "index":True,
            "similarity":"cosine"
        }
    }
}

## Notes:
"""What "analyzer":"english" Means:
The English analyzer is a built-in Elasticsearch analyzer that performs several text processing steps:
1. Tokenization
Splits text into individual words/tokens
Example: "The quick brown fox" → ["the", "quick", "brown", "fox"]
2. Lowercasing
Converts all text to lowercase
Example: "ElasticSearch" → "elasticsearch"
3. English Stop Words Removal
Removes common English words that don't add meaning
Examples: "the", "a", "an", "and", "or", "but", "in", "on", "at"
Example: "The cat is on the mat" → ["cat", "mat"]
4. English Stemming
Reduces words to their root form
Example: "running" → "run"

This analyzer is useful for text search and analysis, especially when dealing with natural language data.

# These searches would all match the same documents:
es.search(index="news", body={
    "query": {"match": {"content": "running"}}  # Matches "run", "runs", "ran"
})

es.search(index="news", body={
    "query": {"match": {"content": "the cat"}}  # Matches "cat" (ignores "the")
})
"""