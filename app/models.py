from mongoengine import Document, StringField, IntField, FloatField, DateTimeField, ListField, ReferenceField, DictField

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