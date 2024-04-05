# import unnitest, app
import unittest
from app import app

class FlaskAppTestCase(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_index_status_code(self):
        response = self.app.post("/", json={"key": "value"})
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
