from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
import requests, json, urllib.parse
import tweepy
app = Flask(__name__)
Bootstrap(app)

# Variables that contains the user credentials to access Twitter API 
ACCESS_TOKEN = '4744703245-ufhQzDCoS46lRldonrc2OjWRWW07uLZMco04FKo'
ACCESS_SECRET = 'TqxZxKm9zv83npkD5g5tyPVTRFxdfBq6TTe2uhPrElNuc'
CONSUMER_KEY = 'aOPaQqCRNdr61S1aruW5uIjXM'
CONSUMER_SECRET = '85vSfNSBiZHDvG3aYeluTS1ye5GURJZx88WiYwFGiHpwmLgiw4'

# Setup tweepy to authenticate with Twitter credentials:

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

# Create the api to connect to twitter with your creadentials
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)
#---------------------------------------------------------------------------------------------------------------------
# wait_on_rate_limit= True;  will make the api to automatically wait for rate limits to replenish
# wait_on_rate_limit_notify= Ture;  will make the api  to print a notification when Tweepyis waiting for rate limits to replenish
#---------------------------------------------------------------------------------------------------------------------


#---------------------------------------------------------------------------------------------------------------------
# The following loop will print most recent statuses, including retweets, posted by the authenticating user and that user’s friends. 
# This is the equivalent of /timeline/home on the Web.
#---------------------------------------------------------------------------------------------------------------------
twitter_status = []
for status in tweepy.Cursor(api.home_timeline).items(1):
	twitter_status.append(status._json)
	
#---------------------------------------------------------------------------------------------------------------------
# Twitter API development use pagination for Iterating through timelines, user lists, direct messages, etc. 
# To help make pagination easier and Tweepy has the Cursor object.
#---------------------------------------------------------------------------------------------------------------------

@app.route('/')
def index():
    return render_template('home.html', data = twitter_status)

