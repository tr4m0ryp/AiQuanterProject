import unittest
from src.recommender import generate_meme_coin_suggestion

class TestRecommender(unittest.TestCase):
    
    def test_generate_meme_coin_suggestion_positive_sentiment(self):
        # Test case with positive sentiment and trending hashtag
        trending_hashtags = [("#dogecoin", 1500), ("#funny", 1200), ("#crypto", 800)]
        sentiment_score = 0.8  # Positive sentiment
        
        suggestion = generate_meme_coin_suggestion(trending_hashtags, sentiment_score)
        
        # Ensure that suggestion is generated correctly
        self.assertIsNotNone(suggestion)
        self.assertEqual(suggestion['meme_coin_name'], "DogecoinCoin")
        self.assertEqual(suggestion['sentiment'], "positive")
        self.assertIn("Create a new meme coin", suggestion['suggestion'])
        
    def test_generate_meme_coin_suggestion_negative_sentiment(self):
        # Test case with negative sentiment and trending hashtag
        trending_hashtags = [("#dogecoin", 1500), ("#funny", 1200), ("#crypto", 800)]
        sentiment_score = -0.8  # Negative sentiment
        
        suggestion = generate_meme_coin_suggestion(trending_hashtags, sentiment_score)
        
        # Ensure that suggestion is generated correctly
        self.assertIsNotNone(suggestion)
        self.assertEqual(suggestion['meme_coin_name'], "DogecoinCoin")
        self.assertEqual(suggestion['sentiment'], "negative")
        self.assertIn("Create a new meme coin", suggestion['suggestion'])
        
    def test_generate_meme_coin_suggestion_neutral_sentiment(self):
        # Test case with neutral sentiment and trending hashtag
        trending_hashtags = [("#dogecoin", 1500), ("#funny", 1200), ("#crypto", 800)]
        sentiment_score = 0.0  # Neutral sentiment
        
        suggestion = generate_meme_coin_suggestion(trending_hashtags, sentiment_score)
        
        # Ensure that suggestion is generated correctly
        self.assertIsNotNone(suggestion)
        self.assertEqual(suggestion['meme_coin_name'], "DogecoinCoin")
        self.assertEqual(suggestion['sentiment'], "neutral")
        self.assertIn("Create a new meme coin", suggestion['suggestion'])

    def test_generate_meme_coin_suggestion_no_trends(self):
        # Test case with no trending hashtags
        trending_hashtags = []
        sentiment_score = 0.5  # Neutral sentiment
        
        suggestion = generate_meme_coin_suggestion(trending_hashtags, sentiment_score)
        
        # Ensure no suggestion is generated when there are no trends
        self.assertIsNone(suggestion)

if __name__ == "__main__":
    unittest.main()
