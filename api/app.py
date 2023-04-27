from flask import Flask
from config import CustomJSONEncoder

from flaskr.routes.test import test_route
from flaskr.routes.get_question import get_question_route
from flaskr.routes.get_avaliable_subjects import get_avaliable_subjects_route


app = Flask(__name__)
app.json_encoder = CustomJSONEncoder

app.register_blueprint(test_route)
app.register_blueprint(get_question_route)
app.register_blueprint(get_avaliable_subjects_route)


if __name__ == '__main__':
    app.run(debug=True)
    