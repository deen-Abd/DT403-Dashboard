import unittest
from app import app

class TestApiEndpoints(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_portfolio_endpoint(self):
        response = self.app.get("/api/portfolio")
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.is_json)

        data = response.get_json()
        self.assertIn("kpis", data)
        self.assertIn("charts", data)
        self.assertIn("top10", data)
        self.assertIn("asof", data)

if __name__ == "__main__":
    unittest.main()
