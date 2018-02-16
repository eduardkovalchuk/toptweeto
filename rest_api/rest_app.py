"""
This is an rest API for toptweet app based on Flask microframework
"""

import sys

from flask import Flask, request, jsonify

sys.path.append("..")

from resources import config
from control import controllers

REST_API = config.REST_API
DELETE = config.DELETE
ADD_HASHTAGS = config.ADD_HASHTAGS
GET_HASHTAGS = config.GET_HASHTAGS
GET_TOP_TWEETS = config.GET_TOP_TWEETS

db_controller = controllers.DbController

toptweet = Flask(__name__)


@toptweet.route(REST_API + ADD_HASHTAGS, methods = ['POST'])
def add_hashtags():
    raw_data = request.data
    hashtags_list = raw_data.split()
    db_controller.write_hashtags(hashtags_list)
    return db_controller.status


@toptweet.route(REST_API + GET_HASHTAGS, methods = ['GET'])
def get_hashtags():
    hashtags = db_controller.get_hashtags()
    return jsonify(hashtags)

if __name__ == "__main__":
    toptweet.run(host='0.0.0.0', port=5000, debug=True)