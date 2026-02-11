import requests
from bs4 import BeautifulSoup

# Step 1: Load the webpage
url = 'https://books.toscrape.com/'  # Example site for practice
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Step 2: Find all book titles
books = soup.find_all('h3')  # Titles are often inside <h3> tags

# Step 3: Print each title
for book in books:
    title = book.find('a')['title']  # 'title' attribute of <a> tag
    print(title)