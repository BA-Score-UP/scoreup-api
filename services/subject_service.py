from flask import make_response
from utils import validate_api_key
from connections import questions_collection

@validate_api_key
def get_subjects_service() -> dict:
    avaliable_subjects = {}
    macro_subject_list = list(questions_collection.distinct('macro_subject'))

    for macro_subject in macro_subject_list:
        micro_subjects = list(questions_collection.find({"macro_subject": macro_subject}).distinct('micro_subject'))
        avaliable_subjects[macro_subject]: dict = micro_subjects

    response_data = {'Subjects': avaliable_subjects}
    return make_response(response_data, 200)

@validate_api_key
def get_question_ammount_by_subjects_service(body: dict) -> dict:

    question_ammount = questions_collection.count_documents(
        body
    )

    response_data = {'Ammount': question_ammount}
    return make_response(response_data, 200)
