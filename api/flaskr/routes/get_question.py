from flask import request
from flaskr.routes.common import Blueprint, CLIENT, response_generator, jsonify
from flaskr.auth import validate_api_key

get_question_route = Blueprint('get_question_route', __name__)

questions_collection = CLIENT.get_database('ScoreUp').get_collection('questions')

@get_question_route.route('/get_question', methods=["POST"])
@validate_api_key
def get_question():

    body = request.get_json()

    if ("macro_subject" not in body and "micro_subject" not in body) or "quantity" not in body:
        return response_generator(
            400,
            "The request should contain at least a macro_subject or a micro_subject and a quantity of questions"
        )

    quantity = body['quantity']
    del body['quantity']
    
    fit_questions = list( questions_collection.find (
        body
    ).limit(quantity))

    response = response_generator(
        status_code=200, 
        message='Success', 
        content_name='Questions', 
        content=fit_questions
    )
    
    return jsonify(response)
    