import unittest
import joblib
from app import app

class TestGDPAPI(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.top_features = joblib.load("model/top_features.pkl")

    def build_sample_input(self):
        return {
            "continent": "Africa",
            "population": 50_000_000,
            **{feature: 2.0 for feature in self.top_features}
        }

    def test_valid_input(self):
        response = self.client.post("/", json=self.build_sample_input())
        self.assertEqual(response.status_code, 200)
        self.assertIn("gdp_per_capita_prediction", response.json)

    def test_missing_field(self):
        bad_input = {"continent": "Africa"}
        response = self.client.post("/", json=bad_input)
        self.assertEqual(response.status_code, 400)

    def test_invalid_continent(self):
        input_data = self.build_sample_input()
        input_data["continent"] = "Atlantis"
        response = self.client.post("/", json=input_data)
        self.assertEqual(response.status_code, 400)

if __name__ == "__main__":
    unittest.main()
