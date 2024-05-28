import requests
import time
import re
from selenium.webdriver.common.by import By
from web_driver import chrome_web_driver
from send_email import send_email
from constants import ZSE_BASE_URL, ISIN, PERCENTAGE_PATTERN, PERCENTAGE_THRESHOLD


def get_stock_change_percentage():
    """
    Retrieve the current stock value and percentage change from the Zimbabwe Stock Exchange (ZSE) website.
    We used Selenium instead of Beautiful Soup 4 because it can handle websites with JavaScript content, allowing us to interact with dynamically loaded elements on the page.

    Returns:
        tuple: A tuple containing two float values:
            - The current stock value.
            - The percentage change in stock value.

    Raises:
        Exception: If the stock element or percentage change element is not found on the webpage.
        Exception: If an error occurs during the HTTP request or any other unexpected error.
    """
    try:
        # Construct the URL for the currency conversion API
        url = f'{ZSE_BASE_URL}?isin={ISIN}'

        # Create Chrome WebDriver instance
        chrome = chrome_web_driver(url=url)

        time.sleep(5)

        # Find stock element on the webpage using XPATH
        stock_element = chrome.find_element(by=By.XPATH,
                                            value='//*[@id="app_indeks"]/section[1]/div/div/div[2]/span[1]')

        # Find percentage element on the webpage using XPATH
        percentage_element = chrome.find_element(by=By.XPATH,
                                                 value='//*[@id="app_indeks"]/section[1]/div/div/div[2]/span[2]')

        # Check if the stock element and percentage element are found
        if stock_element is None:
            raise Exception("\n-- Stock element not found --\n\n")

        if percentage_element is None:
            raise Exception("\n-- Percentage Change element not found --\n\n")

        # Get the text content of the stock element and percentage change element
        stock_text, percentage_text = stock_element.text.strip(), percentage_element.text.strip()

        # Clean the extracted stock and convert it to float
        stock = float(stock_text.replace(",", ""))

        # # Clean the extracted percentage and convert it to float
        # percentage = float(percentage_text.split(" ")[0])

        # Alternatively Use regular expression to extract the percentage value
        match = re.search(PERCENTAGE_PATTERN, percentage_text)
        if not match:
            raise Exception("\n-- Unable to extract percentage change --\n\n")

        # Extracted percentage value
        percentage = float(match.group())

        # Close the web driver session
        chrome.quit()

        return stock, percentage

    except requests.RequestException as e:
        # Handle errors related to HTTP request
        raise Exception(f"\n-- Error during HTTP request: {e}\n\n")

    except Exception as e:
        # Handle other unexpected errors
        raise Exception(f"\n-- Error occurred: {e}\n\n")


def main():
    stock_value, stock_percentage = get_stock_change_percentage()

    if stock_percentage < PERCENTAGE_THRESHOLD:
        subject = "CBX stock has dropped!"

        contents = f"""<h2>CBX stock update</h2>
<p>The value of Croatian government bonds, denoted as <strong>CBX</strong> stock, has seen a minor decrease of less than <strong><em>{PERCENTAGE_THRESHOLD}%</em></strong>.</p>
<p>As per the data available at <span style="text-decoration: underline;">{ZSE_BASE_URL}?isin={ISIN}</span>, the current price stands at <strong>{stock_value}</strong> units.</p>"""

        try:
            send_email(subject, contents)

            print(
                f"\n\n--- CBX stock has dropped by less than {PERCENTAGE_THRESHOLD}%. ---")
            print("\n--- Email sent successfully! ---\n")

        except Exception as e:
            print("\n--- An error occured: ---\n")
            print(f"\n-- Error: {e}\n")

    else:
        message = f"""\n\nThe value of Croatian government bonds, denoted as CBX stock, has seen a change of "{stock_percentage}%".
As per the data available at "{ZSE_BASE_URL}?isin={ISIN}", the current price stands at "{stock_value}" units.\n\n"""

        print(message)


if __name__ == "__main__":
    main()
