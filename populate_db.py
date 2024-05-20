from app import app, User, Course, Lesson, Enrollment
from app.database import db

app.app_context().push()

# Create some test users
users = [
    User(username='testuser1', email='testuser1@example.com', password='password'),
    User(username='testuser2', email='testuser2@example.com', password='password'),
    User(username='testuser3', email='testuser3@example.com', password='password'),
    User(username='instructor1', email='instructor1@example.com', password='password')
]

for user in users:
    db.session.add(user)
db.session.commit()

# Create some test courses
courses = [
    Course(title='Introduction to Python', description='Learn the basics of Python programming',
           instructor_id=users[-1].id),
    Course(title='Web Development with Flask', description='Build web applications using the Flask framework',
           instructor_id=users[-1].id),
    Course(title='Data Analysis with Pandas', description='Explore and analyze data using the Pandas library',
           instructor_id=users[-1].id)
]

for course in courses:
    db.session.add(course)
db.session.commit()

# Create some test lessons
for course in courses:
    for i in range(1, 6):
        lesson = Lesson(
            title=f'Lesson {i}',
            content=f'This is the content for Lesson {i}',
            course_id=course.id
        )
        db.session.add(lesson)
db.session.commit()

# Create some test enrollments
for user in users[:-1]:
    for course in courses:
        enrollment = Enrollment(user_id=user.id, course_id=course.id)
        db.session.add(enrollment)
db.session.commit()
