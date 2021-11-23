import datetime
import tweepy
import json
import os
from dotenv import load_dotenv

load_dotenv()

CONSUMER_KEY = os.getenv('CONSUMER_KEY')
CONSUMER_SECRET = os.getenv('CONSUMER_SECRET')
BEARER_TOKEN = os.getenv('BEARER_TOKEN')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth) # API for V1.1

# Finding place for Canada (3376992a082d67c7)
# places = api.search_geo(query="Canada", granularity="country") 
# print(places)

query = 'place:3376992a082d67c7 -filter:retweets (covid OR vaccination OR pfizer OR moderna OR johnson&johnson OR astrazeneca)'
limit = 2000
tweets = tweepy.Cursor(api.search_tweets, q=query, lang='en', result_type='recent', tweet_mode='extended').items(limit)

l = []
for tweet in tweets:
    l.append(tweet._json)

with open(__file__[:-3] + '_' + datetime.datetime.utcnow().strftime('%Y%m%d_%H%M%S') + ".json", 'w') as ofile:
    json.dump(l, ofile, indent=4)
