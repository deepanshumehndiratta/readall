from readall import app, twitter_api, readability_api

import os


def load_config():
    app.config.from_pyfile('app_data.cfg',silent=True)


def save_config(since_id=0):
    f = os.path.join(os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "instance"), "app_data.cfg")
    f = open(f, "w")
    f.write("FIRST_RUN = False\n")
    f.write("SINCE_ID = %s" % str(since_id))
    f.close()


def save_to_readability(urls):
    urls = urls[::-1]
    for url in urls:
        readability_api.add_bookmark(url=url, allow_duplicates=False)


def get_tweet_urls(tweets=[]):
    urls = []
    for tweet in tweets:
        for url in tweet.get('urls', []):
            urls.append(url)
    return urls


def first_run_twitter_favs():
    local_max_id = max_id = None
    tweets = []
    while True:
        tws = get_twitter_favs(max_id=max_id,save_config_to_file=False)
        try:
            local_max_id = tws[-1].get('id')
        except:
            pass
        if local_max_id == max_id:
            break
        max_id = local_max_id
        for tweet in tws:
            tweets.append(tweet)
    try:
        save_config(since_id=tweets[0].get('id'))
    except:
        pass
    return tweets


def get_twitter_favs(since_id=None,max_id=None,count=200,save_config_to_file=True):
    tweets = []
    for tweet in  twitter_api.GetFavorites(count=count,since_id=since_id,max_id=max_id):
        tweet = tweet.AsDict()
        tweets.append(tweet)
    if save_config_to_file:
        try:
            save_config(since_id=tweets[0].get('id'))
        except Exception, e:
            print str(e)
    return tweets
