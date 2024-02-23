from mongoengine import Document, StringField, IntField

class Workout(Document):
    exercise_name = StringField()
    # Define other fields

class Recipe(Document):
    title = StringField()
    ingredients = StringField()
    # Define other fields
