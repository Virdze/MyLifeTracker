from flask import Blueprint, jsonify
import requests
from app.models.exercise import Exercise
from app.controllers.exercise_controller import ExerciseController

exercise = Blueprint('exercise', __name__)

@exercise.route('/callExercisesAPI', methods=['GET'])
def callExercisesAPI():
    api_url = "https://exercisedb.p.rapidapi.com/exercises/bodyPart/back"

    querystring = {"limit":"100"}

    headers = {
	    "X-RapidAPI-Key": "c8f7c942c6msh71c58f5865ee5c7p188819jsn6bb86afec4f2",
	    "X-RapidAPI-Host": "exercisedb.p.rapidapi.com"
    }

    try:
        response = requests.get(api_url,headers=headers, params=querystring)

        if response.status_code == 200:
            Exercise.save_exercises(Exercise,response.json())
            return jsonify(response.json())
        else:
            return jsonify({
                'errorCode': response.status_code,
                'errorMessage': 'Error calling API' 
            })
    except requests.exceptions.RequestException as e:
        return jsonify({'error': 'An error occurred: {}'.format(e)}), 500    
    
@exercise.get("/workouts/getExercises")
def get_exercises():
    return jsonify(Exercise.get_exercises())

@exercise.get('/workouts/get_gif_url/<name>')
def get_gif_url(name):
    return ExerciseController.get_gif_url(name)
    