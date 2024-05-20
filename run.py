from app import app
from app.users import views
from app.courses import views
from app.lessons import views

if __name__ == '__main__':
    app.run(port=app.config.get('PORT'))
