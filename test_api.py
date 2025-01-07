import unittest
from api import app


class TestApi(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_api(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
