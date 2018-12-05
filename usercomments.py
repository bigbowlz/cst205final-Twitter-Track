#Note:look at the following link to see how to get replies to a tweet
#https://stackoverflow.com/questions/29928638/getting-tweet-replies-to-a-particular-tweet-from-a-particular-user

import json
import tweepy

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
# The following loop will print twitter account "Ring of Elysium"'s most recent tweet/reply in full. 
# This is the equivalent of /timeline/home on the Web.
#---------------------------------------------------------------------------------------------------------------------
twitter_status = []
for status in tweepy.Cursor(api.user_timeline, user_id = "938311640696705024", tweet_mode = "extended").items(20):
    twitter_status.append(status._json)
#The following loop extracts all the tweets of ROE from the list created (twitter_status) and stores them into a new text list.
tweets = []
for i in range(0,len(twitter_status)):
    tweets.append(twitter_status[i]["full_text"])
        
for status in tweets:
    print (status)
#---------------------------------------------------------------------------------------------------------------------#
# The following loop shows all the values in the status dictionary of a tweet
#---------------------------------------------------------------------------------------------------------------------#
'''for i in twitter_status[0]:
    print (f"\n{i}:")
    print (str(twitter_status[0][i]))
'''
#---------------------------------------------------------------------------------------------------------------------#
# The following loop shows all the values in the "user" dictionary of a tweet status
#---------------------------------------------------------------------------------------------------------------------#
'''for i in twitter_status[0]["user"]:
    print (f"\n{i}:")
    print (str(twitter_status[0]["user"][i]))
'''
#---------------------------------------------------------------------------------------------------------------------
# Twitter API development use pagination for Iterating through timelines, user lists, direct messages, etc. 
# To help make pagination easier and Tweepy has the Cursor object.
#---------------------------------------------------------------------------------------------------------------------


