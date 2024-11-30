from collections import Counter
from textblob import TextBlob
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def analyze_sentiment(text: str) -> float:
    """
    Analyze sentiment of a text using TextBlob.
    Returns a sentiment score between -1 (negative) and 1 (positive).
    """
    blob = TextBlob(text)
    return blob.sentiment.polarity  # Sentiment score

def analyze_trends(data):
    """
    Analyze trends in collected data, including sentiment analysis.
    Returns the top 10 trending hashtags and average sentiment.
    """
    hashtags = []
    sentiments = []
    
    for post in data:
        # Extract hashtags from the text
        hashtags.extend([word for word in post['text'].split() if word.startswith('#')])
        
        # Sentiment analysis
        sentiment = analyze_sentiment(post['text'])
        sentiments.append(sentiment)
    
    # Get the top 10 trending hashtags
    trending_hashtags = Counter(hashtags).most_common(10)
    
    # Calculate average sentiment
    avg_sentiment = sum(sentiments) / len(sentiments) if sentiments else 0
    
    return trending_hashtags, avg_sentiment

if __name__ == "__main__":
    # Example data (replace with actual data from data_scraper.py)
    data = [
        {'text': "Check out this funny meme #meme #dogecoin"},
        {'text': "Crypto memes are great! #funny #cryptocurrency"},
        {'text': "This is a hilarious meme! #funny #meme"},
    ]
    
    # Analyzing trends
    trends, sentiment = analyze_trends(data)
    print("Top 10 trending hashtags:", trends)
    print("Average sentiment of posts:", sentiment)
