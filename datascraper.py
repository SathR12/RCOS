import bs4
from bs4 import BeautifulSoup
import requests 


# Previously, this function was very simple and hardcoded only using the requests library
def scrape(link):
    try:
        response = requests.get(link)
        # Note: below is useful for raising a HTTP error
        response.raise_for_status()

        # Hardcoded the first 5000 characters web scraped
        soup = BeautifulSoup(response.text, "html.parser")
        first_5000_characters = soup.text[:100000]

        return first_5000_characters
    
    except:
        print("An error has occurred in the scraping process")

if __name__ == "__main__":
    url = "https://finance.yahoo.com/"
    print(scrape(url))

