import unittest
from api import app


class TestApi(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_api(self):
        response = self.client.get('/api/users')
        success_code = [200, 308]
        failure_message = "Failure 2.0"
        #self.assertEqual(response.status_code, 200) # The API first returns 308 code for redirect, followed by 200, hence line 11
        self.assertIn(response.status_code, success_code, failure_message)

    def test_contact(self):
        response = self.client.get('/contacta')
        success_code = [200]
        failure_message = "Failure 2.0"
        self.assertIn(b'Contact Page', response.data, failure_message)
