import pymongo
import os

def db_cursor():
    MONGO_DB_USERNAME = os.environ["MONGO_DB_USERNAME"]
    MONGO_DB_PASSWORD = os.environ["MONGO_DB_PASSWORD"]
    MONGO_DB_ADDRESS = os.environ["MONGO_DB_ADDRESS"]

    conn_str = f"mongodb+srv://{MONGO_DB_USERNAME}" + \
        f":{MONGO_DB_PASSWORD}@{MONGO_DB_ADDRESS}" + \
        f"/podcast?retryWrites=true&w=majority"

    client = pymongo.MongoClient(conn_str)
    db_cursor = client["podcast"]["guy-raz"]
    return db_cursor