from dotenv import find_dotenv, load_dotenv
import os
from pymongo import MongoClient

load_dotenv(find_dotenv())

USER = os.environ.get("USER")
PASSWORD = os.environ.get("PASSWORD")
CLUSTER = os.environ.get("CLUSTER")

CONECTION = f"mongodb+srv://{USER}:{PASSWORD}@{CLUSTER}.mongodb.net/?retryWrites=true&w=majority"

CLIENT = MongoClient(CONECTION)

if __name__ == '__main__':
    test_db = CLIENT.get_database('test')
    test_collections = test_db.list_collection_names()
    print(f"Testing connection\n {test_collections}")