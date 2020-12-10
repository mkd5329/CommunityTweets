import tweepy
import src.config as config
import numpy as np

from flask import Flask

from flask import request


def getInput():
    #if request.method == 'POST':
    tweet = request.form['tweet']
    print("got tweet: " + str(tweet))
    return tweet


def submit(text):
    consumer_key=config.apiKey()
    consumer_secret_key=config.apiSecret()
    access_token=config.accessKey()
    access_token_secret=config.accessSecret()
    auth = tweepy.OAuthHandler(consumer_key,consumer_secret_key)
    auth.set_access_token(access_token,access_token_secret)
    api = tweepy.API(auth)
    print("got tweet and sending: " + str(text))

    for status in tweepy.Cursor(api.user_timeline).items():
        #print(status.text)
        if("word filter" in status.text):
            try:
                #print(status.text)
                api.destroy_status(status.id)
            except:
                pass


    api.update_status(text)