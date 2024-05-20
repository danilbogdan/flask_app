from flask import render_template, abort
from werkzeug import exceptions

from app import app
from .models import Lesson


@app.errorhandler(exceptions.NotFound)
def http_error_handler(e):
    return 'Error ocured, please try again', 424


@app.get('/lessons/<int:lesson_id>')
def view_lesson(lesson_id):
    lesson = Lesson.query.get(lesson_id)
    if not lesson:
        abort(404)
    return render_template('lessons/view.html', lesson=lesson)


@app.get('/lessons')
def list_lessons():
    lessons = Lesson.query.all()
    return render_template('lessons/list.html', lessons=lessons)
