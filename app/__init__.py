from flask import Flask
from dotenv import load_dotenv
from flask_migrate import Migrate
from app.database import db
from app.users.models import User
from app.lessons.models import Lesson
from app.courses.models import Enrollment, Course


load_dotenv()

app = Flask('LMS')

app.config.from_pyfile('app/config.py')

migrate = Migrate(app, db)

db.init_app(app)

