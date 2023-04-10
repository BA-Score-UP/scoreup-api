from flask import Flask
from flask.json import JSONEncoder
from bson import ObjectId
from flaskr.routes.test import test_route
from flaskr.routes.get_question import get_question_route

class CustomJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        return super().default(obj)

app = Flask(__name__)
app.json_encoder = CustomJSONEncoder

app.register_blueprint(test_route)
app.register_blueprint(get_question_route)


if __name__ == '__main__':
    app.run(debug=True)