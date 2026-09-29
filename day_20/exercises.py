## Day 20, 30daysofpython challenge

# exercises

# 1. Read the url and find the 10 most frequent words.

import requests, re

romeo_and_juliet = 'http://www.gutenberg.org/files/1112/1112.txt'

response = requests.get(romeo_and_juliet)

paragraph = response.text

list_words = re.findall(r'\w+', paragraph)

counter = {}

for word in list_words:
    counter[word] = counter.get(word, 0) + 1

sorted_list = sorted(counter.items(), key=lambda item: item[1], reverse=True)[0:11]

print(sorted_list)

# 2. Read the cats API and cats_api and find:

# i) the min, max, mean, median, standard deviation of cats' weight in metric units

import pandas as pd

cats_api = 'https://api.thecatapi.com/v1/breeds'

response = requests.get(cats_api)

cats = response.json()

cat_weights = []

for cat in cats:
    cat_weights.append(cat['weight'])

df = pd.DataFrame({'values': cat_weights})

val_min = df['values'].min()
val_max = df['values'].max()
val_std = df['values'].std()

# lowk a lot of bs in this one so not really gonna foucs too much on it


