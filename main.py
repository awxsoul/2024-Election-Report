# The libraries used here are requests, beautifulsoup4 and pandas
import requests
from bs4 import BeautifulSoup

url='https://results.eci.gov.in'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
print(soup.prettify()) #to visually understand html content better