# Imports !
from flask import Flask, request, session, g, redirect, url_for, \
	abort, render_template, flash
from wtforms import Form, TextField, validators
import requests
import tweepy

# Configuration. Put in a seperate file later. 
DEBUG = "TRUE"

# Oauth connection to twitter
consumer_key=""
consumer_secret=""
access_token=""
access_token_secret=""
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# app.config.from_envvar('FLASK_SETTING', silent=True)

app = Flask(__name__)
app.config.from_object(__name__)

class TwitterForm(Form):
	twitterName = TextField('Twitter Name', [validators.Length(min=3, max=25)])

@app.route('/', methods=["GET","POST"])
def index():
	form = TwitterForm(request.form)
	if form != None:
		print form.twitterName
	return render_template('test.html')



if __name__ == '__main__':
	app.run(debug=True)


