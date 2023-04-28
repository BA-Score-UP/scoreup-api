from flask import Blueprint, request
from utils.auth import validate_api_key
from services.question_service import *

question_route: Blueprint = Blueprint('question_route', __name__)

@question_route.route('/question/get_filtered', methods=["GET"])
def get_filtered_questions() -> dict:
    return get_filtered_questions_service(request.get_json())

@question_route.route('/question/get_subjects', methods=["GET"])
def get_subjects() -> dict:
    return get_subjects_service()
