import requests
from bs4 import BeautifulSoup
import csv

def scrape_quotes():
    # Target URL for scraping practice
    url = "https://quotes.toscrape.com/"
    
    print(f"Connecting to: {url}...")
    
    # Send HTTP GET request to the website
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code != 200:
        print(f"Error: Unable to fetch data. Status Code: {response.status_code}")
        return
    
    # Parse HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all quote containers on the page
    quote_elements = soup.find_all('div', class_='quote')
    scraped_data = []
    
    print("Extracting data elements...")
    
    # Loop through each container to extract specific details
    for element in quote_elements:
        # Extract text, author, and tags
        text = element.find('span', class_='text').text.strip()
        author = element.find('small', class_='author').text.strip()
        
        tags_elements = element.find_all('a', class_='tag')
        tags = [tag.text.strip() for tag in tags_elements]
        tags_string = ", ".join(tags)
        
        # Append data to the storage list
        scraped_data.append({
            'Quote': text,
            'Author': author,
            'Tags': tags_string
        })
    
    # Define output file name
    csv_filename = "scraped_quotes.csv"
    
    # Write the extracted data into a clean CSV file
    with open(csv_filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['Quote', 'Author', 'Tags'])
        
        writer.writeheader()
        writer.writerows(scraped_data)
        
    print("\n[INFO] Web scraping completed successfully.")
    print(f"[INFO] Dataset saved to file: '{csv_filename}'")
    print(f"[INFO] Total records retrieved: {len(scraped_data)}")

if __name__ == "__main__":
    scrape_quotes()