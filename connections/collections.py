from .mongodb import CLIENT

ScoreUp_DB = CLIENT.get_database('ScoreUp')

questions_collection = ScoreUp_DB.get_collection('questions')
