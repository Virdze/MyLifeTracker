class Config:
    DEBUG = False
    TESTING = False
    MONGODB_SETTINGS = {
        'host': 'mongodb://localhost:27017'  # MongoDB URI
    }

class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = True