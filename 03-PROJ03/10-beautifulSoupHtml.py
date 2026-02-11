import requests
from bs4 import BeautifulSoup

url="https://catalog.feedbooks.com/awards"

response=requests.get(url,headers={"Accept": "text/html"})

parsed_response=BeautifulSoup(response.text,"html.parser")

print(parsed_response.prettify())