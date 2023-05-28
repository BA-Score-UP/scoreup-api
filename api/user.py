from flask import Blueprint, request
from services.user_service import *

user_route: Blueprint = Blueprint('user_route', __name__)

@user_route.route('/user/set_user', methods=["POST"])
def set_user() -> dict:
    body = request.get_json()
    return set_user_service(body)

@user_route.route('/user/set_answer', methods=["POST"])
def set_answer() -> dict:
    body = request.get_json()
    return set_answer_service(body)

@user_route.route('/user/get_answer', methods=["POST"])
def get_answer() -> dict:
    body = request.get_json()
    return get_answer_service(body)

@user_route.route('/user/get_answer_amount', methods=["POST"])
def get_answer_amount() -> dict:
    body = request.get_json()
    return get_answer_amount_service(body)