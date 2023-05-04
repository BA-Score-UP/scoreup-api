from flask import Blueprint, request
from services.subject_service import *

subject_route: Blueprint = Blueprint('subject_route', __name__)

@subject_route.route('/subject/get_subjects', methods=["GET"])
def get_subjects() -> dict:
    return get_subjects_service()

@subject_route.route('/subject/get_question_ammount_by_subjects', methods=["POST"])
def get_question_ammount_by_subjects() -> dict:
    body = request.get_json()
    return get_question_ammount_by_subjects_service(body)