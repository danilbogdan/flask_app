import unittest
from app import app


class CoursesTestCase(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()
    def test_get_courses(self):
        response = self.client.get('/courses')
        self.assertEqual(response.status_code, 200)
        self.assertIn('<p>GET</p>', response.text)

    def test_post_courses(self):
        response = self.client.post('/courses')
        self.assertEqual(response.status_code, 201)
        self.assertIn('<p>POST</p>', response.text)

    def test_get_course_by_id(self):
        course_id = 1
        response = self.client.get(f'/courses/{course_id}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json.get('id'), course_id)