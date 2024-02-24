from mongoengine import Document, StringField, IntField, FloatField, DateTimeField, ListField, ReferenceField

class Exercise(Document):
    name = StringField(required=True)
    description = StringField()
    sets = IntField(required=True)
    reps = IntField(required=True)

class Workout(Document):
    workout_name = StringField(required=True)
    duration = StringField(required=True)
    exercises = ListField(ReferenceField(Exercise))
    description = StringField()
    date = DateTimeField(required=True)

class Recipe(Document):
    title = StringField()
    ingredients = StringField()