import tweepy
import json


def get_data():
    with open("twitter/keys.json", "r") as infile:
        api_key, api_skey, access_token, access_stoken = json.load(infile).values()

    auth = tweepy.OAuthHandler(api_key, api_skey)
    auth.set_access_token(access_token, access_stoken)

    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    name = 'tendobrainrot'
    tweet_id = '1364643149457592320'

    replies = []
    for tweet in tweepy.Cursor(api.search, q='to:' + name, result_type='recent', timeout=999999).items(10):
        if hasattr(tweet, 'in_reply_to_status_id_str'):
            if tweet.in_reply_to_status_id_str == tweet_id:
                replies.append(tweet.text[15:])

    with open("twitter/data.txt", "w") as f:
        f.write('\n'.join(replies))

    return replies
