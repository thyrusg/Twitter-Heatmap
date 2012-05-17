# Imports !
from flask import Flask, request, session, g, redirect, url_for, \
	abort, render_template, flash
import requests
import tweepy

# Configuration. Put in a seperate file later. 
#DEBUG = "TRUE"
# app.config.from_envvar('FLASK_SETTING', silent=True)

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
def index():
	return render_template("index.html")

def collectTweetLocations():
	pass

if __name__ == '__main__':
	app.run()