from flask import make_response, request
from dotenv import find_dotenv, load_dotenv
import os

load_dotenv(find_dotenv())

API_KEY = os.environ.get("API_KEY")

def validate_api_key(func):
    def wrapper(*args, **kwargs):
        api_key = request.headers.get('Api-Key')
        if api_key != API_KEY:
            return make_response({'ERROR': "Invalid API key"}, 401)
        return func(*args, **kwargs)
    return wrapper