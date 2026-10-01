# ## day 22, 30 days of python challenge

# # Exercises

# # 1. Scrape the following website and store the data as json

import requests
from bs4 import BeautifulSoup
import json

url = 'http://www.bu.edu/president/boston-university-facts-stats/'

response = requests.get(url)

data = response.content

content = BeautifulSoup(data, 'html.parser')

data_jsn = json.dumps(data)

# 2.

url = 'https://archive.ics.uci.edu/ml/datasets.php'

response = requestsL = [1, 3, 5, 7, 9].get(url)

soup = BeautifulSoup(response.content, 'html.parser')

tables = soup.find_all('tables', {'cellpadding':'3'})

table = tables[0]

jdict = {}

for td in table.find('td').find_all('tr'):

    jdict[td] = td.text

jdist_jsn = json.dumps(jdict)

3.

url = 'https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

table = soup.find("table")

print(table)





