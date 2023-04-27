from flaskr.routes.common import Blueprint, CLIENT, response_generator, jsonify
from flaskr.auth import validate_api_key

get_avaliable_subjects_route = Blueprint('get_avaliable_subjects_route', __name__)

questions_collection = CLIENT.get_database('ScoreUp').get_collection('questions')

@get_avaliable_subjects_route.route('/get_avaliable_subjects')
@validate_api_key
def get_avaliable_subjects():
    
    avaliable_subjects: dict = {}

    avaliable_macro_subjects:list = list(questions_collection.distinct('macro_subject'))
    
    for macro_subject in avaliable_macro_subjects:
        macro = questions_collection.find({"macro_subject": macro_subject})
        micro_subjects: list = list(macro.distinct('micro_subject'))
        micro_subjects_without_null: list = [item for item in micro_subjects if item is not None]
        avaliable_subjects[macro_subject]: dict = micro_subjects_without_null

    response = response_generator(
        status_code=200, 
        message='Success', 
        content_name='test_collections', 
        content=avaliable_subjects
    )
    
    return jsonify(response)