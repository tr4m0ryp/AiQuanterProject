import unittest
from unittest.mock import patch
from src.data_collection.data_scraper import collect_data

class TestDataScraper(unittest.TestCase):
    @patch('src.data_collection.data_scraper.requests.get')
    def test_collect_data(self, mock_get):
        # Mocking a successful response from the API
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = [{"id": 1, "text": "Test data"}]  # Example data

        url = "https://api.example.com/data"
        data = collect_data(url)

        self.assertIsNotNone(data)  # Check that data is not None
        self.assertEqual(len(data), 1)  # Check that data contains 1 item
        self.assertEqual(data[0]['text'], "Test data")  # Check the text in the data

if __name__ == "__main__":
    unittest.main()
