from mongoengine import Document, StringField, ListField, ReferenceField, DateTimeField, DateTimeField
from models.exercise import Exercise

class Workout(Document):
    workout_name = StringField(required=True)
    duration = StringField(required=True)
    exercises = ListField(ReferenceField(Exercise))
    date = DateTimeField(required=True)