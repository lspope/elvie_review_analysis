import tweepy
import json
import csv


query_list = [
    'elvie train',
    'elvie pump',
    'elvie catch',
    'elvie curve',
    '@elvie',
    '#elvie'
]

query_operators = ' -filter:retweets'

tweet_collection = []

def get_twitter_api(filepath):
    with open(filepath) as f:
        d = json.load(f)
        auth = tweepy.OAuthHandler(consumer_key=d['consumer_key'],
                                   consumer_secret=d['consumer_secret'])
        auth.set_access_token(d['access_token'], d['access_token_secret'])

    api = tweepy.API(auth,
                     retry_count=5,
                     retry_delay=10,
                     retry_errors=set([401, 404, 500, 503]),
                     wait_on_rate_limit=True,
                     wait_on_rate_limit_notify=True)
    return api


def get_desired_tweet_data(tweet):
    id_str = tweet.id_str
    content = tweet.full_text
    if tweet.truncated:
        content = tweet.extended_tweet.full_text

    user_loc = tweet.user.location
    user_screen_name = tweet.user.screen_name
    retweet_count = tweet.retweet_count
    fav_count = 0
    if hasattr(tweet, 'favorite_count'):
        fav_count = tweet.favorite_count

    created_at = tweet.created_at
    tweet_data = {'id_str': id_str,
                 'content': content,
                 'user_loc': user_loc,
                 'user_screen_name': user_screen_name,
                 'retweet_count': retweet_count,
                 'fav_count': fav_count,
                 'created_at': created_at}
    return tweet_data


def get_tweets(api, query):
    for tweet in tweepy.Cursor(api.search,
                               tweet_mode='extended',
                               q=query,
                               result_type='mixed',
                               include_rt=False,
                               timeout=999999).items(2000):

        tweet_collection.append(get_desired_tweet_data(tweet))


if __name__ == "__main__":
    fp = '/home/user/.ssh/twitter_app_capstone.json'

    api = get_twitter_api(filepath=fp)

    for item in query_list:
        get_tweets(api=api, query=item+query_operators)

    print(f"fetched {len(tweet_collection)} tweets")


    keys = tweet_collection[0].keys()

    with open('elvie_tweets.csv', 'w', newline='')  as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(tweet_collection)

    print(f"Wrote tweets to csv file")
