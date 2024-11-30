import requests
import logging
from textblob import TextBlob
from typing import Optional, Dict
import tweepy
import praw
import time

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Twitter API credentials (replace with your own)
TWITTER_API_KEY = 'your-api-key'
TWITTER_API_SECRET_KEY = 'your-api-secret-key'
TWITTER_ACCESS_TOKEN = 'your-access-token'
TWITTER_ACCESS_TOKEN_SECRET = 'your-access-token-secret'

# Reddit API credentials (replace with your own)
REDDIT_CLIENT_ID = 'your-client-id'
REDDIT_SECRET = 'your-secret'
REDDIT_USER_AGENT = 'your-user-agent'

# Sentiment analysis using TextBlob
def analyze_sentiment(text: str) -> float:
    """
    Analyze sentiment of a text using TextBlob.
    Returns a sentiment score between -1 (negative) and 1 (positive).
    """
    blob = TextBlob(text)
    return blob.sentiment.polarity  # Sentiment score

# Twitter Data Collection
def get_twitter_data(query: str, count: int = 100) -> list:
    """
    Collect tweets from Twitter using Tweepy API.
    """
    auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET_KEY)
    auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)

    tweets = tweepy.Cursor(api.search_tweets, q=query, lang="en", tweet_mode="extended").items(count)

    tweet_data = []
    for tweet in tweets:
        tweet_data.append({
            'text': tweet.full_text,
            'likes': tweet.favorite_count,
            'comments': tweet.retweet_count,
            'shares': tweet.user.followers_count,  # As a proxy for shares (followers)
        })
    
    return tweet_data

# Reddit Data Collection
def get_reddit_data(subreddit: str, limit: int = 100) -> list:
    """
    Collect posts from Reddit using PRAW API.
    """
    reddit = praw.Reddit(client_id=REDDIT_CLIENT_ID,
                         client_secret=REDDIT_SECRET,
                         user_agent=REDDIT_USER_AGENT)
    
    posts = reddit.subreddit(subreddit).new(limit=limit)
    
    post_data = []
    for post in posts:
        post_data.append({
            'text': post.title + ' ' + post.selftext,  # Combine title and body text
            'likes': post.ups,
            'comments': post.num_comments,
            'shares': post.subreddit.subscribers,  # As a proxy for shares (subscribers)
        })
    
    return post_data

# Function to collect data from multiple sources
def collect_data_from_sources(sources: list) -> Optional[dict]:
    """
    Collect data from various sources (Twitter, Reddit, etc.).
    """
    collected_data = []
    
    for source in sources:
        if source == 'twitter':
            data = get_twitter_data(query="#meme OR #funny OR #cryptocurrency", count=100)  # Search for general meme-related hashtags
        elif source == 'reddit':
            data = get_reddit_data(subreddit="memes", limit=100)
        else:
            logging.warning(f"Unknown source: {source}")
            continue
        
        # Analyze sentiment for each post
        for post in data:
            post['sentiment_score'] = analyze_sentiment(post['text'])
            collected_data.append(post)
        
    return collected_data

# Save collected data to file
def save_data(data: list, filename: str) -> None:
    """
    Save collected data to a file (e.g., JSON, CSV).
    """
    try:
        with open(filename, 'w') as f:
            json.dump(data, f)
        logging.info(f"Data saved to {filename}")
    except Exception as e:
        logging.error(f"Failed to save data: {e}")

if __name__ == "__main__":
    # Define the sources you want to collect data from
    sources = ['twitter', 'reddit']  # Future sources like Instagram, TikTok can be added here
    data = collect_data_from_sources(sources)
    
    if data:
        save_data(data, 'collected_meme_data.json')
