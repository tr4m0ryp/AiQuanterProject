import unittest
from unittest.mock import patch
from src.data_collection.data_scraper import collect_data_from_sources

class TestDataCollection(unittest.TestCase):
    
    @patch('src.data_collection.data_scraper.get_twitter_data')
    @patch('src.data_collection.data_scraper.get_reddit_data')
    def test_collect_data_from_sources(self, mock_reddit, mock_twitter):
        # Mocking data from Twitter
        mock_twitter.return_value = [
            {'text': 'Check out this meme #dogecoin', 'likes': 1200, 'comments': 150, 'shares': 2000},
            {'text': 'Funny meme about crypto #crypto', 'likes': 500, 'comments': 50, 'shares': 600}
        ]
        
        # Mocking data from Reddit
        mock_reddit.return_value = [
            {'text': 'Crypto memes are great! #funny #dogecoin', 'likes': 1500, 'comments': 200, 'shares': 2500},
            {'text': 'Dogecoin to the moon! #meme', 'likes': 1000, 'comments': 80, 'shares': 1500}
        ]

        # Test data collection from Twitter and Reddit
        sources = ['twitter', 'reddit']
        collected_data = collect_data_from_sources(sources)
        
        # Check if data is being collected correctly (structure check)
        self.assertEqual(len(collected_data), 4)  # 2 from Twitter and 2 from Reddit
        
        # Check that sentiment_score is added (sentiment analysis)
        self.assertIn('sentiment_score', collected_data[0])

        # Check some data (e.g., post text)
        self.assertEqual(collected_data[0]['text'], 'Check out this meme #dogecoin')

if __name__ == "__main__":
    unittest.main()
