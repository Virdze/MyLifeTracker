from mongoengine import Document, StringField, IntField, FloatField, DateTimeField, ListField, ReferenceField



class Workout(Document):
    workout_name = StringField(required=True)
    duration = StringField(required=True)
    description = StringField()
    date = DateTimeField(required=True)

class Recipe(Document):
    title = StringField()
    ingredients = StringField()