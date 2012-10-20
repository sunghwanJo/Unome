from flask_oauth import OAuth
from flask import g
#OAuth configuration
#CONSUMER_KEY = 'PFa4jZPyBEFdKS5vEHwIg'
#CONSUMER_SECRET= 'vzsNg17Pxt6gojxFQTfPizre0LQagMANk73CnS1loQ'
CONSUMER_KEY = 'QdGOizY0OznyHCwL73S2Uw'
CONSUMER_SECRET= 'Pv9CexLxhXmTQauQBEvkA7pHlGz1Kru4we8X9iBVAM'

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

def __get_tweets():
    #JUST REST API, we need to change to STREAMING API
    resp = twitter.get('statuses/home_timeline.json')
    if resp.status == 200:
        # for tweet in tweets 
        #   tweet.screen_name
        #   tweet.text
        g.tweets = resp.data

    else:
        pass
