import random
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def generate_meme_coin_suggestion(trending_hashtags, sentiment_score):
    """
    Generate a suggestion for creating a meme coin based on trending hashtags and sentiment score.
    """
    if not trending_hashtags:
        logging.warning("No trending hashtags found.")
        return None
    
    # Choose a popular hashtag as the base theme for the meme coin
    top_trend = trending_hashtags[0][0]  # First trending hashtag
    
    # Generate a possible meme coin name based on the trend
    coin_name = f"{top_trend.capitalize()}Coin"
    
    # Analyze sentiment to adjust the suggestion
    if sentiment_score > 0.5:
        sentiment_feedback = "positive"
    elif sentiment_score < -0.5:
        sentiment_feedback = "negative"
    else:
        sentiment_feedback = "neutral"
    
    # Generate suggestion
    suggestion = {
        "meme_coin_name": coin_name,
        "trend": top_trend,
        "sentiment": sentiment_feedback,
        "suggestion": f"Create a new meme coin based on the popular trend '{top_trend}'! It has a {sentiment_feedback} sentiment, making it a great candidate for success."
    }
    
    return suggestion

def example_usage():
    # Example trending hashtags and sentiment score (you would get this from trend_detector.py)
    trending_hashtags = [("#dogecoin", 1500), ("#funny", 1200), ("#crypto", 800)]
    sentiment_score = 0.8  # Positive sentiment
    
    # Generate meme coin suggestion
    suggestion = generate_meme_coin_suggestion(trending_hashtags, sentiment_score)
    
    if suggestion:
        logging.info(f"Suggested Meme Coin: {suggestion['meme_coin_name']}")
        logging.info(f"Sentiment: {suggestion['sentiment']}")
        logging.info(f"Suggestion: {suggestion['suggestion']}")

if __name__ == "__main__":
    example_usage()
