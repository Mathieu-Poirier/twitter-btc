import tweepy
import json
import datetime

# Replace with your own Twitter API credentials
consumer_key = 'drvPVO1Z40y8B5qfFi30Qcq4G'
consumer_secret = '5szmzkTQbZqNDvTWLcN9484KNBFBC53qwIKB98mK64Z8Nx7hGI'
access_token = '1746918615138369536-Htc05cNAedZmZZVk0kISqKwZzefo00'
access_token_secret = 'ZcSNnfX0jqj5xWC52eSYDy0NNexvKC9GOlIPEEdh8Vbv2'

# Authenticate with Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

# Define your search query
search_query = 'Bitcoin OR BTC'

# Define the number of tweets you want to gather
num_tweets = 50

# Define the date range (replace with your desired start and end dates)
start_date = datetime.datetime(2024, 1, 15)
end_date = datetime.datetime(2022, 12, 15)

# Open a file to store the tweets
with open('btc_tweets.json', 'w', encoding='utf-8') as file:
    # Loop through each month in the date range
    current_date = start_date
    while current_date < end_date:
        # Define the start and end of the month
        month_start = current_date.replace(day=1)
        month_end = (current_date + datetime.timedelta(days=32)).replace(day=1) - datetime.timedelta(days=1)

        # Search for tweets within the date range
        tweets = tweepy.Cursor(api.search, q=search_query, count=num_tweets, lang='en', since_id=month_start, until=month_end).items(num_tweets)

        # Write each tweet to the file
        for tweet in tweets:
            file.write(json.dumps(tweet._json) + '\n')

        # Move to the next month
        current_date = month_end + datetime.timedelta(days=1)
