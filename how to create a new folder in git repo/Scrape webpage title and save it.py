import requests
from bs4 import BeautifulSoup

def scrape_webpage_title():
    url = input("Enter URL to scrape: ")
    output_file = input("Enter output file path: ")
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.title.string.strip() if soup.title else "No title found"
        
        with open(output_file, 'w') as f:
            f.write(title)
        
        print(f"Title scraped: '{title}'\nSaved to {output_file}")
    
    except requests.RequestException as e:
        print(f"Error accessing the webpage: {str(e)}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Run the function
scrape_webpage_title()