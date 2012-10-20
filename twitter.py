from flask_oauth import OAuth
from flask import g
#OAuth configuration
#Rudy's config
CONSUMER_KEY = 'PFa4jZPyBEFdKS5vEHwIg'
CONSUMER_SECRET= 'vzsNg17Pxt6gojxFQTfPizre0LQagMANk73CnS1loQ'
#SungHwan's config
#CONSUMER_SECRET= 'Pv9CexLxhXmTQauQBEvkA7pHlGz1Kru4we8X9iBVAM'
#CONSUMER_KEY = 'QdGOizY0OznyHCwL73S2Uw'

oauth = OAuth()
# Use Twitter API
twitter = oauth.remote_app('twitter',
    base_url='https://api.twitter.com/1/',
    request_token_url='https://api.twitter.com/oauth/request_token',
    access_token_url='https://api.twitter.com/oauth/access_token',
    authorize_url='https://api.twitter.com/oauth/authorize',
    consumer_key=CONSUMER_KEY,
    consumer_secret=CONSUMER_SECRET
)

def __get_tweets(pages=1):
    DEFAULT_TWEET_COUNT=60
    #JUST REST API, we need to change to STREAMING API
    resp = twitter.get('statuses/home_timeline.json?page=%d&count=%d' %(pages, DEFAULT_TWEET_COUNT))
    if resp.status == 200:
        # for tweet in tweets 
        #   tweet.screen_name
        #   tweet.text
        g.tweets = resp.data

    else:
        pass
