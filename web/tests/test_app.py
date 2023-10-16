import unittest
import os
from app import app

class TestApp(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_redirection(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 302)  # Check if the response is a redirection

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
