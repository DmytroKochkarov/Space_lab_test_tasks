import requests
from bs4 import BeautifulSoup

url = 'https://webscraper.io/test-sites/e-commerce/static/computers/laptops'
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

laptops = soup.find_all('div', class_='col-sm-4 col-lg-4 col-md-4')
for laptop in laptops:
    name = laptop.find('a', class_='title').text.strip()
    price = laptop.find('h4', class_='pull-right price').text.strip()
    description = laptop.find('p', class_='description').text.strip()
    print(name, price, description)