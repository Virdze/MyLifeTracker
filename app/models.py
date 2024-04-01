from mongoengine import Document, StringField, IntField, FloatField, DateTimeField, ListField, ReferenceField, DictField

class Exercise(Document):
    name = StringField(required=True)
    instructions = ListField(StringField(required=True))
    bodyPart = StringField(required=True)
    target = StringField(required=True)
    equipment = StringField(required=True)
    gifURL = StringField(required=True)

    def save_exercises(self, exercises_json):
        for exercise in exercises_json:
            exercise = Exercise(
                name=exercise['name'],
                instructions=exercise['instructions'],
                bodyPart=exercise['bodyPart'],
                target=exercise['target'],
                equipment=exercise['equipment'],
                gifURL=exercise['gifUrl']
            )
            exercise.save()
        return True
    
    def get_exercises(self):
        return Exercise.objects()
    
    def get_gif_url(exercise_name):
        cleared_exercise_name = exercise_name.replace('_',' ')
        exercise = Exercise.objects(name=cleared_exercise_name).first()
        if exercise:
            return exercise.gifURL
        else: 
            return None

class Workout(Document):
    workout_name = StringField(required=True)
    duration = StringField(required=True)
    exercises = ListField(ReferenceField(Exercise))
    date = DateTimeField(required=True)

class MacroNutrients(Document):
    protein = FloatField(required=True)
    carbohydrates = FloatField(required=True) 
    fats = FloatField(required=True)

class MicroNutrients(Document):
    vitamins = DictField(required=True)
    calcium = FloatField(required=True) 
    chloride = FloatField(required=True) 
    magnesium = FloatField(required=True) 
    phosphorus = FloatField(required=True) 
    potassium = FloatField(required=True) 
    sodium = FloatField(required=True)

class Ingredient(Document):
    name = StringField(required=True)
    weight  = FloatField(required=True)
    quantity = IntField(required=True)
    macros = ReferenceField(MacroNutrients)
    micros = ReferenceField(MicroNutrients)

class Recipe(Document):
    title = StringField(required=True)
    description = StringField(required=True)
    cooking_time = StringField(required=True)
    serving_size = IntField(required=True)
    ingredients = ListField(ReferenceField(Ingredient))