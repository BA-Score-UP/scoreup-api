from utils import validate_api_key
from flask import make_response
from connections import *


@validate_api_key
def set_user_service(body: dict) -> dict:
    id: int = body['user_ID']
    
    existing_user = user_collection.find_one({
        'user_hash': id
    })

    if existing_user:
        response_data = {'Message': 'User already exists!'}
        return make_response(response_data, 409)  # HTTP status code 409 for conflict

    new_user: dict = {
        'user_hash': id,
        'wrong_answers': [],
        'correct_answers': []
    }

    user_collection.insert_one(new_user)

    response_data = {'Message': 'User added successfully!'}
    return make_response(response_data, 200)

@validate_api_key
def set_answer_service(body: dict) -> dict:
    id: int = body['user_ID']
    answer_id: int = body['answer_ID']
    status: str = body['status']

    user = user_collection.find_one({'user_hash': id})
    if user:
        if status == 'wrong':
            user_collection.update_one(
                {'user_hash': id},
                {'$pull': {'correct_answers': answer_id}},
                upsert=True
            )
            user_collection.update_one(
                {'user_hash': id},
                {'$addToSet': {'wrong_answers': answer_id}}
            )
        elif status == 'correct':
            user_collection.update_one(
                {'user_hash': id},
                {'$pull': {'wrong_answers': answer_id}},
                upsert=True
            )
            user_collection.update_one(
                {'user_hash': id},
                {'$pull': {'correct_answers': answer_id}},
                upsert=True
            )
            user_collection.update_one(
                {'user_hash': id},
                {'$addToSet': {'correct_answers': answer_id}}
            )

        response_data = {'Message': 'Answer added successfully!'}
        return make_response(response_data, 200)
    else:
        response_data = {'Message': 'User not found!'}
        return make_response(response_data, 404)


@validate_api_key
def get_answer_service(body: dict) -> dict:
    id: int = body['user_ID']
    status: str = body['status']

    user = user_collection.find_one({'user_hash': id})
    if user:
        if status == 'wrong':
            wrong_answers = user.get('wrong_answers', [])
            response_data = {'Wrong Answers': wrong_answers}
        elif status == 'correct':
            correct_answers = user.get('correct_answers', [])
            response_data = {'Correct Answers': correct_answers}
        else:
            response_data = {'Message': 'Invalid status provided!'}
            return make_response(response_data, 400)

        return make_response(response_data, 200)
    else:
        response_data = {'Message': 'User not found!'}
        return make_response(response_data, 404)
