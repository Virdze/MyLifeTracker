from flask import Blueprint, jsonify
from .models import Recipe
from .scraper import scrape_recipes

main = Blueprint('main', __name__)

@main.route('/recipes', methods=['GET'])
def get_recipes():
    recipes = Recipe.objects()
    return jsonify(recipes), 200

@main.route('/scrape', methods=['GET'])
def scrape_and_store_recipes():
    new_recipes = scrape_recipes()
    # Save scraped recipes to MongoDB
    for recipe_data in new_recipes:
        recipe = Recipe(**recipe_data)
        recipe.save()
    return "Recipes scraped and stored successfully", 200
