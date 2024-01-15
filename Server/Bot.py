import tweepy
from datetime import datetime
import json

# To set your environment variables in your terminal run the following lines:
# export 'CONSUMER_KEY'='<your_consumer_key>'
# export 'CONSUMER_SECRET'='<your_consumer_secret>'

consumer_key = 'vgLqIlyenki10gpwRJK6XzEWU'
consumer_secret = 'eedonMfWNE5KliJCL1j5m1sBkmGmZaf7SzofKolK2GlVS1TjxM'
access_token = '1746918615138369536-vbKqnMBYVKOJ83CWGUhVuYe9nxDlRA'
access_token_secret = 'JMPEvaVoErbxlV76sLqIUJYaMwTPUPSeU1T7GLNWknzMT'

# Authenticate with Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Get current date in the desired format
current_date = datetime.now().strftime("%Y-%m-%d")

# Your reminder message
reminder_message = f"Hey guys, it's {current_date}! Whatever project you're working on right now, remember to keep going strong!"

# Post the tweet
api.update_status(reminder_message)

# Log the tweet to a JSON file
log_entry = {
    'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    'tweet': reminder_message
}


log_file_path = 'tweet_log.json'

try:
    with open(log_file_path, 'a') as log_file:
        json.dump(log_entry, log_file)
        log_file.write('\n')
    print(f'Tweet logged to {log_file_path}')
except Exception as e:
    print(f'Error logging tweet: {e}')