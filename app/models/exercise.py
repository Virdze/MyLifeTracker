from mongoengine import Document, StringField, ListField
class Exercise(Document):
    api_id = StringField(required=True)
    name = StringField(required=True)
    instructions = ListField(StringField(required=True))
    bodyPart = StringField(required=True)
    target = StringField(required=True)
    equipment = StringField(required=True)
    gifURL = StringField(required=True)

    def save_exercises(self, exercises_json):
        for exercise in exercises_json:
            exercise = Exercise(
                api_id = exercise['id'],
                name=exercise['name'],
                instructions=exercise['instructions'],
                bodyPart=exercise['bodyPart'],
                target=exercise['target'],
                equipment=exercise['equipment'],
                gifURL=exercise['gifUrl']
            )
            exercise.save()
        return True
    
    def get_exercises():
        return Exercise.objects()
    
    def get_exercise_by_id(id):
        return Exercise.objects(id=id)
    
    def get_exercise_by_name(name):
        return Exercise.objects(name=name)
    
