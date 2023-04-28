from utils import validate_api_key
from flask import make_response
from random import sample
from connections import *


@validate_api_key
def get_filtered_questions_service(body: dict) -> dict:
    quantity: int = body['quantity']
    del body['quantity']

    filtered_questions = list(questions_collection.find(
        body
    ))

    response_data = {'Questions': sample(filtered_questions, quantity)}
    return make_response(response_data, 200)


@validate_api_key
def get_subjects_service() -> dict:
    avaliable_subjects = {}
    macro_subject_list = list(questions_collection.distinct('macro_subject'))

    for macro_subject in macro_subject_list:
        micro_subjects = list(questions_collection.find({"macro_subject": macro_subject}).distinct('micro_subject'))
        avaliable_subjects[macro_subject]: dict = micro_subjects

    response_data = {'Subjects': avaliable_subjects}
    return make_response(response_data, 200)
