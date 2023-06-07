from utils import validate_api_key
from flask import make_response
from connections import *
from bson import ObjectId

@validate_api_key
def get_user_performance_service(body: dict):
    id: str = body['user_ID']
    user = user_collection.find_one({'user_hash': id})
    if not user:
        response_data = {
            'error': 'User not found.'
        }
        return make_response(response_data, 404)

    micro_subject_performance: dict = {}

    correct_list: list = user.get('correct_answers', [])
    for answer_id in correct_list:
        answer = questions_collection.find_one({'_id': ObjectId(answer_id)})
        answer_micro_subject = answer.get('micro_subject')
        if answer_micro_subject in micro_subject_performance:
                micro_subject_performance[answer_micro_subject]['made'] += 1
                micro_subject_performance[answer_micro_subject]['correct'] += 1
        else:
            micro_subject_performance[answer_micro_subject] = {
                'made': 1,
                'correct': 1
            }

    wrong_list: list = user.get('wrong_answers', [])
    for answer_id in wrong_list:
        answer = questions_collection.find_one({'_id': ObjectId(answer_id)})
        answer_micro_subject = answer.get('micro_subject')
        if answer_micro_subject in micro_subject_performance:
                micro_subject_performance[answer_micro_subject]['made'] += 1
        else:
            micro_subject_performance[answer_micro_subject] = {
                'made': 1,
                'correct': 0
            }

    response_data = {
        'Performance': micro_subject_performance
    }

    return make_response(response_data, 200)