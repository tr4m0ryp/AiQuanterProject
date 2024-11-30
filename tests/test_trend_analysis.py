import unittest
from src.trend_analysis.trend_detector import analyze_trends

class TestTrendAnalyzer(unittest.TestCase):
    def test_analyze_trends(self):
        data = [
            {'text': "Check out this new meme #meme #funny"},
            {'text': "Funny meme! #funny #meme"},
            {'text': "Just another post #meme"},
        ]
        trends = analyze_trends(data)
        self.assertEqual(trends[0][0], '#meme')  # Check that the top trend is #meme
        self.assertEqual(trends[1][0], '#funny')  # Check that the second trend is #funny

if __name__ == "__main__":
    unittest.main()
