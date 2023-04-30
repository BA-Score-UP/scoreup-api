from flask import Blueprint, request
from services.question_service import *

question_route: Blueprint = Blueprint('question_route', __name__)

@question_route.route('/question/get_filtered', methods=["GET"])
def get_filtered_questions() -> dict:
    body = request.get_json()
    return get_filtered_questions_service(body)
