import tweepy
import json


def get_data():
    with open("twitter/keys.json", "r") as infile:
        api_key, api_skey, access_token, access_stoken = json.load(infile).values()

    auth = tweepy.OAuthHandler(api_key, api_skey)
    auth.set_access_token(access_token, access_stoken)

    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
