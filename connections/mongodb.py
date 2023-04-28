import os
from flask import make_response
from pymongo import MongoClient
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())
try:
    CONECTION = f"mongodb+srv://{os.environ.get('USER')}:{os.environ.get('PASSWORD')}@{os.environ.get('CLUSTER')}.mongodb.net/?retryWrites=true&w=majority"
    CLIENT = MongoClient(CONECTION)
except:
    make_response({'ERROR': "Invalid credentials"}, 401)