from bs4 import BeautifulSoup
import json

# Read the HTML file
with open("index.html", "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser")

# List to store the extracted data
products = []

# Find all relevant div elements
divs = soup.find_all("div", class_="sg-col-20-of-24 s-result-item s-asin sg-col-0-of-12 sg-col-16-of-20 sg-col s-widget-spacing-small sg-col-12-of-16")

# Iterate through each div and extract data
for div in divs:
    # Initialize data fields
    link = ''
    title = ''
    rating = ''
    price = ''
    
    # Try to find the image link
    img = div.find("img", class_="s-image")
    if img and 'src' in img.attrs:
        link = img["src"]
    
    # Try to find the title
    span_title = div.find("span", class_="a-size-medium a-color-base a-text-normal")
    if span_title:
        title = span_title.text.strip()
    
    # Try to find the rating
    span_rating = div.find("span", class_="a-icon-alt")
    if span_rating:
        rating = span_rating.text.strip()
    
    # Try to find the price
    span_price = div.find("span", class_="a-price-whole")
    if span_price:
        price = span_price.text.strip()
    
    # Append the extracted data to the products list
    products.append({
        "link": link,
        "title": title,
        "rating": rating,
        "price": price
    })

# Write the extracted data to data.json
with open("data.json", "w", encoding="utf-8") as json_file:
    json.dump(products, json_file, ensure_ascii=False, indent=4)

print(f"Successfully extracted {len(products)} products and saved to data.json")
