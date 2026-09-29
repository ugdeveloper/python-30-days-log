## day 20, pip - python package manager

# pip is preferred installer program
    
import pandas
import numpy

# opening url

import webbrowser

url_lists = [
    'http://www.python.org',
    'https://www.linkedin.com/in/asabeneh',
    'https://github.com/ugdeveloper'
]

for url in url_lists:
    webbrowser.open_new_tab(url)

## info from url

import requests

url = 'https://www.w3.org/TR/PNG/iso_8859-1.txt'

response = requests.get(url)

print(response)
print(response.status_code)
print(response.headers)
print(response.text)

url = 'https://restcountries.eu/rest/v2/all'

response = requests.get(url)
print(response)
print(response.status_code)
countries = response.json()
print(countries[:1])

# creating packages
# __init__.py file, followed by whatever imports you create

# Useful packages

# database -> SQLAlchemy, pip install SQLAlchemy

# web development -> django, pip instlal django, flask, pip install flask

# html parser, beautiful soup, pip install beautifulsoup4. pyquery, pip install pyquery

# data analysis:

    # Numpy
    # Pandas
    # SciPy
    #Scikit
    # TensorFlow
    # Keras
    # PyTorch

# network

    # requests
