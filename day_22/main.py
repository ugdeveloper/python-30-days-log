## day 22, web scrapping

import requests
from bs4 import BeautifulSoup

url = 'https://archive.ics.uci.edu/datasets'

# Use requests to fetch data from url

response = requests.get(url)
content = response.content

soup = BeautifulSoup(content, 'html.parser')
print(soup.title)
print(soup.title.get_text())
print(soup.body)
print(response.status_code)

tables = soup.find_all('table', {'cellpadding':'3'})

table = tables[1]

for td in table.find('tr').find_all('td'):
    print(td.text)


