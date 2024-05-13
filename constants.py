import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()


# Fetching the sender's email and password from environment variables
SENDER = os.getenv('USER')  # Fetching the sender's email address
PASSWORD = os.getenv('PASSWORD')  # Fetching the sender's email password  
# Setting up the recipient's email address
# Disposable email service used from: https://temp-mail.org/en/
RECEIVER = "bayaxo6553@godsigma.com"

# Specify the path to the ChromeDriver executable
# Make sure to download the appropriate ChromeDriver version matching existing Chrome version
CHROMEDRIVER_PATH = Path("./chromedriver-win64") / "chromedriver.exe"

# base url for Zagreb Stock Exchange, Inc. in Croatia
ZSE_BASE_URL = "https://zse.hr/en/indeks-366/365"

# The International Securities Identification Number (ISIN) 'HRZB00ICBEX6' corresponds to a Croatian government bond.
# Its symbol is "CBX"
ISIN = "HRZB00ICBEX6"

# This pattern to extract the percentage change value
PERCENTAGE_PATTERN = r'([+-]?\d*\.\d+|\d+)'