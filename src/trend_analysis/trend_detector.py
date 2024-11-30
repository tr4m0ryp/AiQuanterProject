import requests
from collections import Counter

def analyze_trends(data):
    """Function to analyze trends in collected data."""
    # Example: Count how many times a specific hashtag appears
    hashtags = []
    for post in data:
        hashtags.extend([word for word in post['text'].split() if word.startswith('#')])
    
    return Counter(hashtags).most_common(10)  # Return top 10 hashtags

if __name__ == "__main__":
    # Example data, should come from collect_data function
    data = [
        {'text': "Check out this new meme #meme #funny"},
        {'text': "Funny meme! #funny #meme"},
        {'text': "Just another post #meme"},
    ]
    
    trends = analyze_trends(data)
    print("Top 10 trending hashtags:", trends)
