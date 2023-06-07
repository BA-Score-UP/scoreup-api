from flask import Blueprint, request
from services.statistics_service import *

statistics_route: Blueprint = Blueprint('statistics_route', __name__)

@statistics_route.route('/statistics/get_user_performance', methods=["POST"])
def get_user_performance() -> dict:
    body = request.get_json()
    return get_user_performance_service(body)