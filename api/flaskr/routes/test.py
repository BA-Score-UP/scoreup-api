from flaskr.routes.common import Blueprint, CLIENT, response_generator, jsonify

test_route = Blueprint('test_route', __name__)

@test_route.route('/test')
def test():
    test_db = CLIENT.get_database('test')
    test_collections = test_db.list_collection_names()
    
    response = response_generator(
        status_code=200, 
        message='Success', 
        content_name='test_collections', 
        content=test_collections
    )
    
    return jsonify(response)