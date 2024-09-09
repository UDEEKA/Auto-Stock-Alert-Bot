import requests
from bs4 import BeautifulSoup
import re

url = 'https://finance.yahoo.com/quote/AAPL?p=AAPL'

response = requests.get(url)
html_content = response.text

soup = BeautifulSoup(html_content, 'html.parser')

price_element = soup.find('fin-streamer', {'data-field': 'regularMarketPrice'})
price_text = price_element.text

price = float(re.sub('[^0-9.]', '', price_text))

print(f'Current Apple stock price: ${price}')
