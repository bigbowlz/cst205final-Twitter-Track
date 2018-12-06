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


# print twitter account "Ring of Elysium"'s most recent tweets/replies in full. 
'''twitter_status = []
for status in tweepy.Cursor(api.user_timeline, user_id = "938311640696705024", tweet_mode = "extended").items(20):
    twitter_status.append(status._json)
#The following loop extracts all the tweets of ROE from the list created (twitter_status) and stores them into a new text list.
tweets = []
for i in range(0,len(twitter_status)):
    tweets.append(twitter_status[i]["full_text"])
        
for status in tweets:
    print (status)


print("----------------------------------")
'''

#search "en" tweets associated with a specific account (replying to or mentioning that account) and the keyword given, and store the result. items in "text_result" list are strings.
def get_comments(keyword, account):
    status_results = []
    if (keyword == "") or (account == ""):
        keyword = input("Keyword: ")
        account = input("User ID of the twitter account you are monitoring (e.g. @CallofDuty): ")
    for status in tweepy.Cursor(api.search, q = f'{keyword} {account} -filter:retweets', Since="2018-10-00", lang = "en", show_user = True, tweet_mode = "extended").items(100000):
        status_results.append(status._json)

    #extract and show all the text 
    text_results = []
    for i in range(0,len(status_results)):
        text_results.append(status_results[i]["full_text"])
    return text_results
            


