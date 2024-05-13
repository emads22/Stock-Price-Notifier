import requests
import time
import re
from selenium.webdriver.common.by import By
from web_driver import chrome_web_driver
from constants import ZSE_BASE_URL, ISIN, PERCENTAGE_PATTERN


def get_stock_change_percentage():
    """
    Retrieve the percentage change in stock value from the Zimbabwe Stock Exchange (ZSE) website.

    Returns:
        float: The percentage change in stock value.

    Raises:
        Exception: If the percentage change element is not found on the webpage.
        Exception: If an error occurs during the HTTP request or any other unexpected error.
    """
    try:
        # Construct the URL for the currency conversion API
        url = f'{ZSE_BASE_URL}?isin={ISIN}'

        # Create Chrome WebDriver instance
        chrome = chrome_web_driver(url=url)

        time.sleep(5)

        # Find percentage element on the webpage using CSS Selector
        percentage_element = chrome.find_element(by=By.CSS_SELECTOR,
                                                 value='#app_indeks > section.page-heading > div > div > div.stock-page-center > span.stock-trend.trend-drop')

        # Check if the percentage element is found
        if percentage_element is None:
            raise Exception("\n-- Percentage Change element not found --\n\n")

        # Get the text content of the percentage change element
        percentage_text = percentage_element.text

        # # Clean the extracted percentage and convert it to float
        # percentage = float(percentage_text.strip().split(" ")[0])

        # Alternatively Use regular expression to extract the percentage value
        match = re.search(PERCENTAGE_PATTERN, percentage_text)
        if not match:
            raise Exception("\n-- Unable to extract percentage change --\n\n")

        # Extracted percentage value
        percentage = float(match.group())

        # Close the web driver session
        chrome.quit()

        return percentage

    except requests.RequestException as e:
        # Handle errors related to HTTP request
        raise Exception(f"\n-- Error during HTTP request: {e}\n\n")

    except Exception as e:
        # Handle other unexpected errors
        raise Exception(f"\n-- Error occurred: {e}\n\n")


def main():
    driver = get_driver()
    time.sleep(2)
    element = driver.find_element(by="xpath",
                                  value='//*[@id="app_indeks"]/section[1]/div/div/div[2]/span[2]')
    text = str(clean_text(element.text))

    # if(float(text) < -0.10):
    #     send_email(str(text))


if __name__ == "__main__":
    test = get_stock_change_percentage()

    print(test)

    # main()
