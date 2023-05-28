from utils import validate_api_key
from flask import make_response
from random import sample
from connections import *
from bson import ObjectId


@validate_api_key
def get_filtered_questions_service(body: dict) -> dict:
    quantity: int = body['quantity']
    del body['quantity']

    filtered_questions = list(questions_collection.find(body))

    response_data = {'Questions': sample(filtered_questions, quantity)}
    return make_response(response_data, 200)


@validate_api_key
def get_questions_by_id_service(body: dict) -> dict:
    question_ids = body['questions_ids']

    object_ids = [ObjectId(id_) for id_ in question_ids]

    questions = list(questions_collection.find({'_id': {'$in': object_ids}}))

    response_data = {'Questions': questions}
    return make_response(response_data, 200)
