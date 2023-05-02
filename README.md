# ScoreUP RESTful API

## Main libraries used

1. Pymongo[srv] - A library for interacting with MongoDB, with added support for SRV records.
2. Flask - A micro web framework that allows building web applications quickly and easily.
3. Python-dotenv - A library for loading environment variables from a .env file into the OS environment variables.
4. Gunicorn - A UNIX server that allows multiple worker processes to handle requests simultaneously.
5. Pipenv - A package manager that provides a virtual environment, dependency resolver, and lockfile for managing dependencies in Python projects.

## Folder structure

```tree
.
├─── api/
├─── services/
├─── connections/
├─── utils/
├─── app.py
└─── config.py
```

* api/ - holds all endpoints and routes.
* services/ - where the routes logic are implementes.
* connections/ - app external connections (such as DB).
* utils/ - methods that are used all around the app.
* app.py - flask application initialization.
* config.py - all global app settings.

## Running

1. Clone the repository: ```git clone https://github.com/BA-Score-UP/scoreup-api.git```
2. Make sure that pipenv is installed: ```pip install pipenv```
3. Install dependencies via pipenv: ```pipenv install```
4. Start the virtual environment: ```pipenv shell```
5. Start the local debug server: ```python app.py```

## Usage

⚠️ Make sure having a valid "Api-Key" in your Header ⚠️

### Question endpoints

#### GET .../question/get_filtered:

eg. REQUEST:

```json
{
    "macro_subject": "Português",
    "micro_subject": "Literatura",
    "quantity": 1
}
```

eg. RESPONSE:

```json
{
    "Questions": [
        {
            "_id": "640e6fc22176975a1e70df4e",
            "answer": 2,
            "explanation": "Explanation string",
            "macro_subject": "Português",
            "micro_subject": "Literatura",
            "options": [ ],
            "statement": {
                "command": "statement Command",
                "hasImg": true,
                "text": "statement Text"
            },
            "year": "2022"
        }
    ]
}
```

### Subject endpoints

#### GET .../subject/get_subjects:

eg. RESPONSE:

```json
{
    "Subjects": {
        "Ciências Humanas": [ ],
        "Ciências da Natureza": [ ],
        "Inglês": [ ],
        "Matemática": [ ],
        "Português": [ ]
    }
}
```

#### GET .../subject/get_question_ammount_by_subject:

eg. REQUEST:

```json
{
    "macro_subject": "Português",
    "micro_subject": "Arte e Literatura"
}
```

eg. RESPONSE:

```json
{
    "Ammount": 2
}
```
