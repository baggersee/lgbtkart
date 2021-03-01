from twitter.get_data import get_replies
from itertools import product
import pandas as pd
import json

# Load responses if available. If not, scrape them
try:
    with open("twitter/replies.txt", "r") as infile:
        replies = infile.read().split("\n")
except FileNotFoundError:
    # I have to imporove the data colection since I have to delete all the time
    print("Data not found, creating new data")
    replies = get_replies(10000)
print("Data loaded correctly")


# Load column values and accepted keywords (Sexualities)
with open("cfg/sexuality.json", "r") as infile:
    sexuality_dict = json.load(infile)
    columns = list(sexuality_dict.keys())

# Load index values and accepted keywords (Mario Kart Characters)
with open("cfg/kart.json", "r") as infile:
    kart_dict = json.load(infile)
    indices = list(kart_dict.keys())

results = pd.DataFrame(0, index=indices, columns=columns)

for reply in replies:
    i, j = [], []
    # The sorting algorithm is not very good, creates wrong matches e.g. (lesbian) -> (lesbian and bi)
    for sex_key, sex_kwrds in sexuality_dict.items():
        if any([s in reply for s in sex_kwrds]):
            i.append(sex_key)
    for kart_key, kart_kwrds in kart_dict.items():
        if any([k in reply for k in kart_kwrds]):
            j.append(kart_key)

    reply_indices = list(product(i, j))
    if reply_indices:
        for idx in reply_indices:
            results.at[idx[1], idx[0]] += 1

indices.append("TOTAL")
for c in columns:
    total = results[c].sum()
    results.at["TOTAL", c] = total

columns.append("TOTAL")
for i in indices:
    total = results.loc[i].sum()
    if total == 0:
        results = results.drop(i)
    else:
        results.at[i, "TOTAL"] = total

print(results)
results.to_csv('results.csv', encoding="utf-8", sep=",")