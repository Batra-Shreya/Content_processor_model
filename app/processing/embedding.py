import os
from huggingface_hub import InferenceClient
from dotenv import load_dotenv
load_dotenv()

client = InferenceClient(
    provider="hf-inference",
    api_key=os.getenv("HF_TOKEN"),
)

text = "That is a happy person"

result = client.feature_extraction(
   text,
   #model="sentence-transformers/all-MiniLM-L6-v2",
   # model="Qwen/Qwen3-Embedding-0.6B",
    model="mixedbread-ai/mxbai-embed-large-v1",
)

print(result)
print(result.shape)