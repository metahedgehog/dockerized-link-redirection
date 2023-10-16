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

    def test_count_file_missing(self):
        # Rename the count.txt file to simulate its absence
        os.rename('/app/data/count.txt', '/app/data/count.txt.bak')
        response = self.app.get('/counter', data={'data': '/app/data'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Visits: 0', response.data)  # Check if the count is 0

        # Restore the count.txt file if it was renamed
        if os.path.exists('/app/data/count.txt.bak'):
            os.rename('/app/data/count.txt.bak', '/app/data/count.txt')

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
