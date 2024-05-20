import flask

from app import app
from flask import request, abort, render_template
from .models import Course, Enrollment


@app.route('/courses', methods=['GET', 'POST'])
def list_courses():
    if request.method == 'POST':
        result = '<p>POST</p>'
        return result, 201
    elif request.method == 'GET':
        courses = Course.query.all()
        return render_template('courses/list_courses.html', courses=courses)


@app.get('/courses/<int:course_id>')
def view_course(course_id):
    course = Course.query.get(course_id)
    if not course:
        abort(404)
    lessons = course.lessons.all()

    user_id = flask.session.get('user_id')
    if user_id:
        enrollment = Enrollment.query.filter_by(user_id=user_id, course_id=course_id).first()
    else:
        enrollment = None

    return render_template('courses/view.html', course=course, lessons=lessons, enrollment=enrollment)


# @app.get('/courses/<int:course_id>')
# def get_course(course_id):
#     cookies = request.cookies
#     if cookies.get('visited'):
#         return f'You have already visited this page {course_id}'
#     resp = make_response(f'You have not visited this page {course_id}')
#     resp.set_cookie('visited', 'true', max_age=60)
#     return resp
