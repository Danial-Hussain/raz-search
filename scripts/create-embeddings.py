from sentence_transformers import SentenceTransformer

import sys
sys.path.insert(0, '..')

from server.mongo import db_cursor

model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

cursor = db_cursor()

documents = cursor.find(projection = {"description": 1})

embeddings = [
    (doc["_id"], model.encode(doc["description"]).tolist()) 
    for doc in documents
]

result = [
    cursor.update_one({"_id": id}, {"$set": {"embedding": embedding}})
    for id, embedding in embeddings
]