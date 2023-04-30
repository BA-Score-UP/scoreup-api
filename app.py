from flask import Flask
from config import *
from api import *

app = Flask(__name__)
app.json_encoder = CustomJSONEncoder

app.register_blueprint(question_route)
app.register_blueprint(subject_route)

if __name__ == '__main__':
    app.run(debug=True)
