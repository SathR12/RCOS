from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

# Code is based off https://brightdata.com/blog/how-tos/scrape-yahoo-finance-guide 

debug = False

def scrape(stock):

    url = f"https://finance.yahoo.com/quote/{stock}"
    options = Options()
    # These options need to be set so there is no handshake failed error for the protocol
    options.add_argument("--ignore-certificate-errors")
    # Laptop does not have a dedicated gpu
    options.add_argument("--disable-gpu") 
    # Disables UI to reduce additional overhead when scraping 
    options.add_argument("--headless")

    # Drivers for selenium to interact with google chrome
    # Note: this looks at the current version of Google Chrome installed on machine to find drivers
    # Creates chrome browser instance for selenium to interact with
    driver = webdriver.Chrome(service = ChromeService(ChromeDriverManager().install()), options = options)
    driver.get(url)

    try:
        # Scraping current stock price
        # Code below waits until html elements are rendered before beginning the scraping process
        stock_price_element = WebDriverWait(driver, 10).until(
            # This needs to be passed into selenium to scrape a specific part of the CSS 
            # This can be retrieved by simply inspecting the yahoo finance page 
            # The fin-streamer tag is a container for the stock price data, selenium finds the fin-streamer element for the specified stock
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, f'fin-streamer[data-symbol = "{stock}"][data-field = "regularMarketPrice"]')
            )
        )

        stock_price = stock_price_element.text

        # Scraping previous close of the stock
        previous_close_element =  WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, f'fin-streamer[data-symbol = "{stock}"][data-field = "regularMarketPreviousClose"]')
            )
        )

        previous_close_price = previous_close_element.text

        # Saving into dictionary format to feed the scraped data into the model 
        data = {
            "stock_symbol": stock, 
            "current_stock_price": stock_price,
            "previous_close_price": previous_close_price
        }

        if debug:
            print(f"Stock Price for {stock}: {stock_price}")
            print(f"Previous Close for {stock}: {previous_close_price}")
            print(f"Printing dictionary of formatted entries:\n{data}")
        
        return data


    except:
        print(f"An error has occurred in the scraping process")


if __name__ == "__main__":
    scrape("AAPL")
