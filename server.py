from flask import Flask, render_template

import json
import tweepy

CONSUMER_KEY = "LWjtYO4gHNeqAlHymYvHdvBnU"
CONSUMER_SECRET = "	IGaSCoho0wKXAd7jLpzHHtwFE81Cx8oP7iEgtQmnGZzsVVOiLi"
ACCESS_KEY = "739483674-NSFAHYvm4A4YjMgv4WnZAye0af6gvWbuSTyZsmZt"
ACCESS_SECRET = "epjWxpTcQwUfqPGeX6nztehL2FFFwGnmgBYxcfKg4BsXw"

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

api = tweepy.API(auth, wait_on_rate_limit=True)

public_tweets = api.home_timeline(count=100)

for tweet in public_tweets:
    print(tweet.text)

app = Flask(__name__ , static_folder='./react/dist' , template_folder='./react/dist')

@app.route("/")
def main():
    return render_template('index.html')

if __name__ == "__main__":
    app.run()