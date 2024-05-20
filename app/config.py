import os

SECRET_KEY = os.getenv('SECRET_KEY', 'secret1')
DEBUG = os.getenv('DEBUG', False)
print(type(DEBUG))
PORT = os.getenv('PORT')
SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')