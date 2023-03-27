from flask import request
from flaskr.routes.common import Blueprint, CLIENT, response_generator, jsonify

get_question_route = Blueprint('get_question_route', __name__)

questions_collection = CLIENT.get_database('ScoreUp').get_collection('questions')

@get_question_route.route('/get_question', methods=["POST"])
def get_question():

    body = request.get_json()

    if "macro_subject" not in body:
        return response_generator(
            400,
            "The macro subject parameter MUST be included"
        )
    
    fit_questions = list(
        questions_collection.find(body)
    )

    response = response_generator(
        status_code=200, 
        message='Success', 
        content_name='Questions', 
        content=fit_questions
    )
    
    return jsonify(response)