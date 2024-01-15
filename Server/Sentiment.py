from textblob import TextBlob
import json

def analyze_sentiment(text):
    analysis = TextBlob(text)
    return analysis.sentiment.polarity

# Example usage
with open('btc_tweets.json', 'r', encoding='utf-8') as file:
    for line in file:
        tweet_json = json.loads(line)
        tweet_text = tweet_json['text']
        sentiment_score = analyze_sentiment(tweet_text)
        print(f'Tweet: {tweet_text}\nSentiment Score: {sentiment_score}\n')
