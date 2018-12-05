from datetime import datetime
from flask import Flask, render_template, url_for
from form import UserInput

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'


@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def index():
    form = UserInput()
    return render_template("index.html", form = form)

@app.route('/sentiment')
def sentiment():
    
    return render_template("sentiment.html", title = "Sentiments")

@app.route('/tweets')
def tweets():
    
    return render_template("tweets.html", title = "Tweets")

@app.route('/about')
def about():
    
    return render_template("about.html", title = "About")

if __name__ == '__main__':
    app.run(debug = True)
