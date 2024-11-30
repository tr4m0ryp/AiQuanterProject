import unittest
from src.trend_analysis.trend_detector import analyze_trends

class TestTrendAnalyzer(unittest.TestCase):
    
    def test_analyze_trends(self):
        # Example data
        data = [
            {'text': "Check out this funny meme #dogecoin #meme"},
            {'text': "Crypto memes are great #crypto #dogecoin"},
            {'text': "Just another meme #meme"},
        ]
        
        # Analyzing trends
        trends, sentiment = analyze_trends(data)
        
        # Check top trending hashtags
        self.assertEqual(trends[0][0], '#dogecoin')  # #dogecoin should be the top trend
        self.assertEqual(trends[1][0], '#meme')  # #meme should be the second trend
        
        # Check sentiment value (average)
        self.assertGreaterEqual(sentiment, -1)  # Sentiment should be between -1 and 1
        self.assertLessEqual(sentiment, 1)

    def test_no_trends(self):
        # Test with no posts
        data = []
        trends, sentiment = analyze_trends(data)
        
        # No trends should be found, neutral sentiment
        self.assertEqual(trends, [])
        self.assertEqual(sentiment, 0)

if __name__ == "__main__":
    unittest.main()
