import requests
from bs4 import BeautifulSoup
from time import sleep

for page_number in range(2,4):
# Step 1: Load the webpage
    print("\nPage Number:", page_number)
    url = "https://books.toscrape.com/catalogue/page-"+str(page_number)+".html"  # Example site for practice
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Step 2: Find all book titles
    books = soup.find_all('h3')  # Titles are often inside <h3> tags

    # Step 3: Print each title
    for book in books:
        title = book.find('a')['title']  # 'title' attribute of <a> tag
        print(title)
    sleep(1)