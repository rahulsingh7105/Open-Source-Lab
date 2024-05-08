import tweepy

# Authenticate
consumer_key = 'YOUR_CONSUMER_KEY'
consumer_secret = 'YOUR_CONSUMER_SECRET'
access_token = 'YOUR_ACCESS_TOKEN'
access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'

auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# Scrape tweets from a user's timeline
username = 'target_user'
tweet_count = 10  # Number of tweets to scrape

tweets = api.user_timeline(screen_name=username, count=tweet_count, tweet_mode='extended')

for tweet in tweets:
    print(tweet.full_text)
