from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class UserInput(FlaskForm):
    keyword = StringField("Keyword", validators=[DataRequired(), Length(min=2, max=20)])
    numTweets = StringField("Number of tweets", validators=[DataRequired(), Length(min=1, max=20)])
    account = StringField("Account", validators=[DataRequired(), Length(min=1, max=20)])
    submit = SubmitField("Submit")
