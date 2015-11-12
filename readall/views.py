from readall import app
from tasks import get_twitter_favs, first_run_twitter_favs, load_config, get_tweet_urls, save_to_readability
from readability import auth

@app.route("/")
def index():
    load_config()
    tweets = []
    try:
        if app.config.get('FIRST_RUN'):
            tweets = first_run_twitter_favs()
        else:
            tweets =  get_twitter_favs(since_id=app.config.get('SINCE_ID'))
        save_to_readability(get_tweet_urls(tweets))
        return "Saved %s link(s) to readability" % str(len(tweets))
    except Exception, e:
        return str(e)