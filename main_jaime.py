from twitter.get_data import get_replies
from pprint import pprint
import pandas as pd
import json

try:
    with open("twitter/replies.txt", "r") as infile:
        replies = infile.read().split("\n")
except FileNotFoundError:
    replies = get_replies(100)

pprint(replies)

with open("cfg/sexuality.json", "r") as infile:
    sexuality_dict = json.load(infile)

with open("cfg/kart.json", "r") as infile:
    kart_dict = json.load(infile)

results = pd.DataFrame(0, index=list(kart_dict.keys()),
                       columns=list(sexuality_dict.keys()))

for reply in replies:
    pass

pprint(results)
