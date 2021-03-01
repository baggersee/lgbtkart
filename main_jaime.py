from twitter.get_data import get_replies
import json

try:
    with open("twitter/replies.txt", "r") as infile:
        replies = infile.read().split("\n")
except FileNotFoundError:
    replies = get_replies(100)

print(replies)

with open("sexuality.json", "r") as infile:
    sexuality_dict = json.load(infile)

with open("kart.json", "r") as infile:
    kart_dict = json.load(infile)

results = {key: 0 for key in sexuality_dict}

print(results)
