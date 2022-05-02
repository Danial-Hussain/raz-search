import pymongo
from dotenv import dotenv_values

def db_cursor():
    config = dotenv_values(".env")
    MONGO_DB_USERNAME = config["MONGO_DB_USERNAME"]
    MONGO_DB_PASSWORD = config["MONGO_DB_PASSWORD"]
    MONGO_DB_ADDRESS = config["MONGO_DB_ADDRESS"]

    conn_str = f"mongodb+srv://{MONGO_DB_USERNAME}" + \
        f":{MONGO_DB_PASSWORD}@{MONGO_DB_ADDRESS}" + \
        f"/podcast?retryWrites=true&w=majority"

    client = pymongo.MongoClient(conn_str)
    db_cursor = client["podcast"]["guy-raz"]
    return db_cursor