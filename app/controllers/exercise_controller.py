from models.exercise import Exercise
import requests#
from flask import jsonify
class ExerciseController:

    def get_gif_url(exercise_name):
        exercise_id = Exercise.get_exercise_by_name(exercise_name).api_id
        
        if exercise_id:
            api_url = f'https://exercisedb.p.rapidapi.com/exercises/exercise/{exercise_id}'

            headers = {
	            "X-RapidAPI-Key": "c8f7c942c6msh71c58f5865ee5c7p188819jsn6bb86afec4f2",
	            "X-RapidAPI-Host": "exercisedb.p.rapidapi.com"
            }

            try:
                response = requests.get(api_url,headers=headers)

                if response.status_code == 200:
                    
                    return jsonify(response.gifUrl)
                else:
                    return jsonify({
                        'errorCode': response.status_code,
                        'errorMessage': response.message 
                    })
            except requests.exceptions.RequestException as e:
                return jsonify({'error': 'An error occurred: {}'.format(e)}), 500    
        else: 
            return None