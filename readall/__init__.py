from flask import Flask
from flask.ext.mail import Mail
from readability import ReaderClient

import logging
import twitter

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('readall.default_settings')
app.config.from_pyfile('application.cfg', silent=True)

app.logger.setLevel(logging.INFO)
app.logger.addHandler(logging.StreamHandler())

mail = Mail(app)

twitter_api = twitter.Api(consumer_key=app.config['TWITTER_CONSUMER_KEY'],
                  consumer_secret=app.config['TWITTER_CONSUMER_SECRET'],
                  access_token_key=app.config['TWITTER_ACCESS_TOKEN'],
                  access_token_secret=app.config['TWITTER_ACCESS_TOKEN_SECRET'])

readability_api = ReaderClient(token_key=app.config['READABILITY_TOKEN_KEY'],
                               token_secret=app.config['READABILITY_TOKEN_SECRET'],
                               consumer_key=app.config['READABILITY_CONSUMER_KEY'],
                               consumer_secret=app.config['READABILITY_CONSUMER_SECRET'])

__import__('readall.views')