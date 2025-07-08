from elasticsearch import Elasticsearch
import os
from index_mapping import indexMapping

es = Elasticsearch(
    "http://localhost:9200",
    basic_auth=("elastic", os.getenv("ELASTIC_PASSWORD")),
    verify_certs=False,
    ssl_show_warn=False
)
        
info = es.info()
print(f"Connected to Elasticsearch")
print(f"Cluster: {info['cluster_name']}")
print(f"Version: {info['version']['number']}")

es.indices.create(index="news", mappings=indexMapping)


