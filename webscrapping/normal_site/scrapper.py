import requests
from bs4 import BeautifulSoup
import json

# Base URL of the website
base_url = "https://books.toscrape.com/catalogue/page-{}.html"

# List to store all book data
all_books = []

# Function to scrape a single page
def scrape_page(page_number):
    url = base_url.format(page_number)
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        books = soup.find_all("article", class_="product_pod")
        for book in books:
            # Extract book details
            title = book.h3.a["title"]
            price = book.find("p", class_="price_color").text
            availability = book.find("p", class_="instock availability").text.strip()
            rating = book.p["class"][1]
            # Get the relative link and construct the full link
            relative_link = book.h3.a["href"]
            book_link = f"https://books.toscrape.com/catalogue/{relative_link}"
            
            # Append book data to the list
            all_books.append({
                "title": title,
                "price": price,
                "availability": availability,
                "rating": rating,
                "link": book_link
            })
        return True  # Indicates successful scraping of the page
    return False  # Indicates failure

# Loop through pages
page_number = 1
while True:
    print(f"Scraping page {page_number}...")
    success = scrape_page(page_number)
    if not success:  # Break the loop if no more pages
        print("No more pages to scrape.")
        break
    page_number += 1

# Save data to a JSON file
output_file = "books_data.json"
with open(output_file, "w") as file:
    json.dump(all_books, file, indent=4)

print(f"Scraping completed. Data saved to {output_file}")
