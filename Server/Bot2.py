from requests_oauthlib import OAuth1Session
from datetime import datetime

# Your Twitter API credentials
consumer_key = 'vgLqIlyenki10gpwRJK6XzEWU'
consumer_secret = 'eedonMfWNE5KliJCL1j5m1sBkmGmZaf7SzofKolK2GlVS1TjxM'

# Be sure to replace the text of the with the text you wish to Tweet.
# You can also add parameters to post polls, quote Tweets, Tweet with reply settings,
# and Tweet to Super Followers in addition to other features.
current_date = datetime.now().strftime("%Y-%m-%d")
tweet_text = f"Hey guys, it's {current_date}! Whatever project you're working on right now, remember to keep going strong!"
payload = {
    "text": tweet_text,  # Use "text" instead of "status"
    "reply_settings": "mentionedUsers",  # Set your preferred reply settings
    "geo": {"place_id": "5a110d312052166f"},  # Set your preferred location information
    # Add other parameters as needed (e.g., "media", "poll", "for_super_followers_only", etc.)
}

# Get request token
request_token_url = "https://api.twitter.com/oauth/request_token?oauth_callback=oob&x_auth_access_type=write"
oauth = OAuth1Session(consumer_key, client_secret=consumer_secret)

try:
    fetch_response = oauth.fetch_request_token(request_token_url)
except ValueError:
    print("There may have been an issue with the consumer_key or consumer_secret you entered.")

resource_owner_key = fetch_response.get("oauth_token")
resource_owner_secret = fetch_response.get("oauth_token_secret")
print("Got OAuth token: %s" % resource_owner_key)

# Get authorization
base_authorization_url = "https://api.twitter.com/oauth/authorize"
authorization_url = oauth.authorization_url(base_authorization_url)
print("Please go here and authorize: %s" % authorization_url)
verifier = input("Paste the PIN here: ")

# Get the access token
access_token_url = "https://api.twitter.com/oauth/access_token"
oauth = OAuth1Session(
    consumer_key,
    client_secret=consumer_secret,
    resource_owner_key=resource_owner_key,
    resource_owner_secret=resource_owner_secret,
    verifier=verifier,
)
oauth_tokens = oauth.fetch_access_token(access_token_url)

access_token = oauth_tokens["oauth_token"]
access_token_secret = oauth_tokens["oauth_token_secret"]

# Make the request
oauth = OAuth1Session(
    consumer_key,
    client_secret=consumer_secret,
    resource_owner_key=access_token,
    resource_owner_secret=access_token_secret,
)

# Making the request to post a tweet
response = oauth.post(
    "https://api.twitter.com/2/tweets",  # Updated to Twitter API v2 endpoint
    json=payload,
)

# Check for errors
if response.status_code != 201:
    raise Exception(f"Request returned an error: {response.status_code} {response.text}")

print("Tweet posted successfully!")


