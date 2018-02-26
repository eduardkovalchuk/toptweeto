"""
This is an rest API for toptweet app based on Flask microframework
"""

#--------------------------------------------------------------------------------------------------

import sys
from flask import Flask, request, jsonify

sys.path.append("..")

from resources import config
from control.puppeteer import Puppeteer

#--------------------------------------------------------------------------------------------------

REST_API = config.REST_API
DELETE_HASHTAGS = config.DELETE
ADD_HASHTAGS = config.ADD_HASHTAGS
GET_HASHTAGS = config.GET_HASHTAGS
GET_TOP_TWEETS = config.GET_TOP_TWEETS

#--------------------------------------------------------------------------------------------------

toptweet = Flask(__name__)

puppeteer = Puppeteer()

#--------------------------------------------------------------------------------------------------

@toptweet.route(REST_API + ADD_HASHTAGS, methods = ['POST'])
def add_hashtags():
    hashtags = request.get_json()
    status = puppeteer.write_hashtags(hashtags)
    return jsonify(status)


@toptweet.route(REST_API + DELETE_HASHTAGS, methods = ['DELETE'])
def delete_hashtags():
    hashtags = request.get_json()
    status = puppeteer.delete_hashtags(hashtags)
    return jsonify(status)


@toptweet.route(REST_API + GET_HASHTAGS, methods = ['GET'])
def get_hashtags():
    hashtags = puppeteer.get_hashtags()
    return jsonify(hashtags)


@toptweet.route(REST_API + GET_TOP_TWEETS, methods = ['GET'])
def get_top_tweets():
    top_tweets = puppeteer.get_top_tweets()
    return jsonify(top_tweets)   

#--------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    toptweet.run(host='0.0.0.0', port=5000, debug=True)