# ScoreUP RESTful API 
## Main libraries used:
1. Pymongo[srv] - A ibrary for interacting with MongoDB, with added support for SRV records.
2. Flask - A micro web framework that allows building web applications quickly and easily.
3. Python-dotenv - Alibrary for loading environment variables from a .env file into the OS environment variables.
4. Gunicorn - A server for Unix that allows multiple worker processes to handle requests simultaneously.
5. Pipenv - A package manager that provides a virtual environment, dependency resolver, and lockfile for managing dependencies in Python projects.

## Project structure:
```
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
* utils/ - methos that are used all around the app.
* app.py - flask application initialization.
* config.py - all global app settings.

## Running 
1. Clone repository.
    1.5. pip install pipenv
2. pipenv install.
3. pienv shell.
4. Start server by running python app.py

## Usage
Make shure having the "Api-Key" in your Header
### Question endpoints
GET .../question/get_filtered
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
            "explanation": "Expalnation string",
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

## Subject endpoints
GET .../subject/get_subjects
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

GET .../subject/get_question_ammount_by_subject
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