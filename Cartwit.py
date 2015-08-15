# -*- coding: utf8 -*-

# Import modules
import twitter
import json
from accounts import *

# Connection data
app = account["twitter"]
api = twitter.Api(consumer_key=app["api_key"],
                  consumer_secret=app["api_secret"],
                  access_token_key=app["token"],
                  access_token_secret=app["token_secret"])


tweets = api.GetUserTimeline("Whenrow")

tweets = [tweet.AsDict() for tweet in tweets]
with open('tweets.json', 'w') as outfile:
        json.dump(tweets, outfile)
