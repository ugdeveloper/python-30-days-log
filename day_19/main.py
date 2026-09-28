# Day 19 - 30daysofpy

# Exercises

# 1. Write a function which counts the number of lines and number of words in a text.
# All the files are in the data folder.

# def read_file(file_directory: str):

#     try:
#         with open(file_directory) as f:
#             print(f.read())
#     except Exception as e:
#         print(e)

# 2. Read the countries_data.json data file in data directory, create a function that finds the ten most spoken languages

import json

with open('./day_19/countries_data.json', 'r', encoding='utf-8') as file:
    data = file.read()

country_dtc = json.loads(data)

counts = {}

for country in country_dtc:
    for language in country['languages']:
        counts[language] = counts.get(language, 0) + 1

top_ten = sorted(counts.items(), key=lambda item: item[1], reverse=True)[0:11]

# print(top_ten)

# 3. Read the countries_data.json data file in data directory, create a function that creates a list of the ten most populated countries

with open('./day_19/countries_data.json', 'r', encoding='utf-8') as file:
    data = file.read()

country_dtc = json.loads(data)

count_pairs = []

for country in country_dtc:
    count_pairs.append({'country': country['name'], 'population': country['population']})

top_ten = sorted(count_pairs, key=lambda x: x['population'], reverse=True)[0:11]

print(top_ten)

## not finishing ts so tedious (sobbing)




