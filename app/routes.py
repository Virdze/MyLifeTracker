from flask import Blueprint, jsonify, render_template
from .models import Recipe, Exercise
from .scraper import scrape_recipes
import requests

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')


@main.route('/callExercisesAPI', methods=['GET'])
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
    
@main.route("/getExercises", methods=["GET"])
def get_exercises():
    return jsonify(Exercise.get_exercises(Exercise))

@main.get('/workouts/<name>/get_gif_url')
def get_gif_url(name):
    url = Exercise.get_gif_url(name)
    if url:
        return jsonify({'gifURL' : url})
    else :
        return jsonify({'error' : 'Exercise not found'})

# @main.route('/recipes', methods=['GET'])
# def get_recipes():
#     recipes = Recipe.objects()
#     return jsonify(recipes), 200
# 
# @main.route('/scrape', methods=['GET'])
# def scrape_and_store_recipes():
#     new_recipes = scrape_recipes()
#     # Save scraped recipes to MongoDB
#     for recipe_data in new_recipes:
#         recipe = Recipe(**recipe_data)
#         recipe.save()
#     return "Recipes scraped and stored successfully", 200
