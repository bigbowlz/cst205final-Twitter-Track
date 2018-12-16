import sys, tweepy, csv, re, json, os
from textblob import TextBlob
import matplotlib.pyplot as plt
import twitter_credentials as credentials


class SentimentAnalysis:

    def __init__(self, keyword, account, numTweets):
        self.tweets = []
        self.tweetText = []
        self.result = {}
        self.text = []
        self.keyword = keyword
        self.account = account
        self.numTweets = numTweets

    def DownloadData(self):
        # authenticating
        consumerKey = credentials.CONSUMER_KEY
        consumerSecret = credentials.CONSUMER_SECRET
        accessToken = credentials.ACCESS_TOKEN
        accessTokenSecret = credentials.ACCESS_SECRET
        
        auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
        auth.set_access_token(accessToken, accessTokenSecret)
        api = tweepy.API(auth)

        # input for term to be searched and how many tweets to search
        searchTerm = self.keyword
        '''search_change = input(f'Current keyword on track is {searchTerm}, wanna change the keyword? (Y/N)')
        while search_change != "N":
            if search_change == "Y":
                searchTerm = input("Enter Keyword/Tag to search about: ")
                search_change = "N"
            else:
                search_change = input(f'Please enter Y or N. \nCurrent keyword on track is {searchTerm}, wanna change the keyword? (Y/N)')'''

        account = self.account
        '''account_change = input(f'Current account on track is {account}, wanna change the account? (Y/N)')
        while account_change != "N":
            if account_change == "Y":
                account = input("Enter Keyword/Tag to search about: ")
                account_change = "N"
            else:
                account_change = input(f'Please enter Y or N. \nCurrent keyword on track is {account}, wanna change the account? (Y/N)')'''
        
        start_t = "2018-04-01"
        # searching for tweets
        #filter: mentioning the account
        status_results = []
        for status in tweepy.Cursor(api.search, q = f'{searchTerm} @{account} -filter:retweets', Since = start_t, lang = "en", tweet_mode = "extended").items(self.numTweets):
            status_results.append(status._json)

        #filter: replying to the account
        for status in tweepy.Cursor(api.search, q = f'{searchTerm} to:{account} -filter:retweets', Since = start_t, lang = "en", tweet_mode = "extended").items(self.numTweets):
            status_results.append(status._json)
        #print (status_results)
        
        #extract and show all the text 
        text_results = []
        for i in range(0,len(status_results)):
            text_results.append(status_results[i]["full_text"])
            self.text.append(status_results[i]["full_text"])
       
        # Open/create a file to append data to
        csvFile = open('result.csv', 'a')

        # Use csv writer
        csvWriter = csv.writer(csvFile)


        # creating some variables to store info
        polarity = 0
        positive = 0
        wpositive = 0
        spositive = 0
        negative = 0
        wnegative = 0
        snegative = 0
        neutral = 0
        NoOfTerms = len(text_results)

   
        # iterating through tweets fetched
        for tweet in range(len(text_results)):
            #Append to temp so that we can store in csv later. I use encode UTF-8
            self.tweetText.append(self.cleanTweet(text_results[tweet]).encode('utf-8'))
            
            analysis = TextBlob(text_results[tweet])
            
            polarity += analysis.sentiment.polarity  # adding up polarities to find the average later

            if (analysis.sentiment.polarity == 0):  # adding reaction of how people are reacting to find average later
                neutral += 1
            elif (analysis.sentiment.polarity > 0 and analysis.sentiment.polarity <= 0.3):
                wpositive += 1
            elif (analysis.sentiment.polarity > 0.3 and analysis.sentiment.polarity <= 0.6):
                positive += 1
            elif (analysis.sentiment.polarity > 0.6 and analysis.sentiment.polarity <= 1):
                spositive += 1
            elif (analysis.sentiment.polarity > -0.3 and analysis.sentiment.polarity <= 0):
                wnegative += 1
            elif (analysis.sentiment.polarity > -0.6 and analysis.sentiment.polarity <= -0.3):
                negative += 1
            elif (analysis.sentiment.polarity > -1 and analysis.sentiment.polarity <= -0.6):
                snegative += 1


        # Write to csv and close csv file
        csvWriter.writerow(self.tweetText)
        csvFile.close()

        # finding average of how people are reacting
        positive = self.percentage(positive, NoOfTerms)
        wpositive = self.percentage(wpositive, NoOfTerms)
        spositive = self.percentage(spositive, NoOfTerms)
        negative = self.percentage(negative, NoOfTerms)
        wnegative = self.percentage(wnegative, NoOfTerms)
        snegative = self.percentage(snegative, NoOfTerms)
        neutral = self.percentage(neutral, NoOfTerms)

        # finding average reaction
        polarity = polarity / NoOfTerms

        # printing out data
        self.result["report_title"] = f'How people are reacting on "{searchTerm}" by analyzing {NoOfTerms} tweets:'
        
        #self.result.append("General Report: ")

        if (polarity == 0):
            self.result["general"] = "General Sentiment: Neutral"
        elif (polarity > 0 and polarity <= 0.3):
            self.result["general"] = "General Sentiment: Weakly Positive"
        elif (polarity > 0.3 and polarity <= 0.6):
            self.result["general"] = "General Sentiment: Positive"
        elif (polarity > 0.6 and polarity <= 1):
            self.result["general"] = "General Sentiment: Strongly Positive"
        elif (polarity > -0.3 and polarity <= 0):
            self.result["general"] = "General Sentiment: Weakly Negative"
        elif (polarity > -0.6 and polarity <= -0.3):
            self.result["general"] = "General Sentiment: Negative"
        elif (polarity > -1 and polarity <= -0.6):
            self.result["general"] = "General Sentiment: Strongly Negative"

        self.result["de_report"] = "Detailed Report: "
        r_details = []
        r_details.append(str(positive) + "% people thought it was positive")
        r_details.append(str(wpositive) + "% people thought it was weakly positive")
        r_details.append(str(spositive) + "% people thought it was strongly positive")
        r_details.append(str(negative) + "% people thought it was negative")
        r_details.append(str(wnegative) + "% people thought it was weakly negative")
        r_details.append(str(snegative) + "% people thought it was strongly negative")
        r_details.append(str(neutral) + "% people thought it was neutral")
        self.result["report_stat"] = r_details

        self.plotPieChart(positive, wpositive, spositive, negative, wnegative, snegative, neutral, searchTerm, NoOfTerms)



    def cleanTweet(self, tweet):
        # Remove Links, Special Characters etc from tweet
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) | (\w +:\ / \ / \S +)", " ", tweet).split())

    # function to calculate percentage
    def percentage(self, part, whole):
        temp = 100 * float(part) / float(whole)
        return format(temp, '.2f')
    
    def plotPieChart(self, positive, wpositive, spositive, negative, wnegative, snegative, neutral, searchTerm, noOfSearchTerms):
        labels = ['Positive [' + str(positive) + '%]', 'Weakly Positive [' + str(wpositive) + '%]','Strongly Positive [' + str(spositive) + '%]', 'Neutral [' + str(neutral) + '%]',
                  'Negative [' + str(negative) + '%]', 'Weakly Negative [' + str(wnegative) + '%]', 'Strongly Negative [' + str(snegative) + '%]']
        sizes = [positive, wpositive, spositive, neutral, negative, wnegative, snegative]
        colors = ['yellowgreen','lightgreen','darkgreen', 'gold', 'red','lightsalmon','darkred']
        patches, texts = plt.pie(sizes, colors=colors, startangle=90)
        plt.legend(patches, labels, loc="best")
        plt.title('How people are reacting on "' + searchTerm + '" by analyzing ' + str(noOfSearchTerms) + ' Tweets.')
        plt.axis('equal')
        plt.tight_layout()
        '''
        if os.path.exists("static/sentiment.png"):
            os.remove("static/sentiment.png")
            plt.savefig('static/sentiment.png')
        else:
            plt.savefig('static/sentiment.png')
        '''
        plt.savefig(f'static/sentiment_{self.keyword}.png')
    def getText(self):
        return self.text
    
    def getResult(self):
        return self.result
