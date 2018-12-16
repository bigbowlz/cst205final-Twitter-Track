from datetime import datetime
from flask import Flask, render_template, url_for, redirect
from form import UserInput
from sentiment_analysis import SentimentAnalysis

analysis = []
tweets = []
app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'




@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def index():
    global analysis
    global tweets
    global keyword
    form = UserInput()
    
    if form.validate_on_submit():
        #gets data from the form
        keyword = form.keyword.data
        numTweets = int(form.numTweets.data)
        account = form.account.data
        
        Sentiment = SentimentAnalysis(keyword, account, numTweets)
        Sentiment.DownloadData()
        
        analysis = Sentiment.getResult()
        tweets = Sentiment.getText()
        
        return redirect('/sentiment')
    return render_template("index.html", form = form)

@app.route('/sentiment')
def sentiment():
    
    return render_template("sentiment.html", title = "Sentiments", analysis = analysis, keyword = f'sentiment_{keyword}.png')

@app.route('/tweets')
def tweets():
    
    return render_template("tweets.html", title = "Tweets", tweets = tweets)

@app.route('/about')
def about():
    
    return render_template("about.html", title = "About")

if __name__ == '__main__':
    app.run(debug = True)
