from mongo import db_cursor
from bson.json_util import dumps

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

cursor = db_cursor()

model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

app = FastAPI()
origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware, 
    allow_origins = origins, 
    allow_credentials = True, 
    allow_methods = ["*"], 
    allow_headers = ["*"]
)

@app.get("/all/")
async def all():
    results = cursor.find(
        projection = {
            "name": 1, 
            "description": 1
        }
    )
    return dumps(list(results))

@app.get("/latest-episodes/")
async def latest_episodes(limit: int = 10):
    results = cursor.find(
        limit = limit, 
        projection = {"embedding": 0}
    ).sort("release_date", -1)
    return dumps(list(results))

@app.get("/search/")
async def search(query: str, limit: int = 10):
    documents = list(cursor.find())
    embedding = model.encode(query).flatten().reshape(1, -1)
    documents.sort(
        key = lambda x: cosine_similarity(
            embedding, np.array(x["embedding"]).reshape(1, -1)), 
            reverse = True
        )
    _ = [doc.pop("embedding") for doc in documents]
    documents = documents[0:limit]
    return dumps(documents)