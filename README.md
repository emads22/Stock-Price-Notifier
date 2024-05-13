# Stock Price Notifier

## Overview
Stock Price Notifier is a Python script designed to monitor the percentage change in the value of Croatian government bonds and notify the user via email if the percentage change falls below a specified threshold. It fetches the stock value and percentage change from the [Zagreb Stock Exchange (ZSE) website](https://zse.hr/en/) and sends an email notification if the percentage change is below a certain threshold. The International Securities Identification Number (ISIN) `HRZB00ICBEX6` corresponds to a Croatian government bond. Its symbol is `CBX`. This script monitors this stock here but it applies to any stock on any platform given the right configuration.

## Features
- **Real-time Monitoring**: The script retrieves real-time data from the ZSE website to monitor the percentage change in the value of Croatian government bonds.
- **Email Notification**: If the percentage change falls below a specified threshold, the script sends an email notification to the user.
- **Disposable Email Service**: Users can generate a disposable email from the provided website in `constants.py` for receiving notifications.
- **JavaScript Execution**: The script utilizes Selenium to execute JavaScript content on the website, unlike Beautiful Soup, ensuring accurate data extraction.
- **Customizable Parameters**: This project can be applied to monitor the percentage change of any stock from any website and with any threshold defined by the user.
- **Rich Email Format**: Email notifications are sent in HTML format, providing a rich and visually appealing display of stock information.

## Setup
1. Clone the repository.
2. Ensure Python 3.x is installed.
3. Install the required dependencies using `pip install -r requirements.txt`.
4. Configure the necessary parameters such as `SENDER`, `PASSWORD`, and `RECEIVER` in `constants.py`.
5. Download the appropriate ChromeDriver version matching your Chrome browser version and specify the path in `constants.py`.
6. Run the script using `python main.py`.

## Usage
1. Run the script using `python main.py`.
2. The script will monitor the percentage change in the value of Croatian government bonds.
3. If the percentage change falls below the specified threshold, an email notification will be sent to the recipient specified in `constants.py`.

## Contributing
Contributions are welcome! Here are some ways you can contribute to the project:
- Report bugs and issues
- Suggest new features or improvements
- Submit pull requests with bug fixes or enhancements

## Author
- Emad &nbsp; E>
  
  [<img src="https://img.shields.io/badge/GitHub-Profile-blue?logo=github" width="150">](https://github.com/emads22)

## License
This project is licensed under the MIT License, which grants permission for free use, modification, distribution, and sublicense of the code, provided that the copyright notice (attributed to [emads22](https://github.com/emads22)) and permission notice are included in all copies or substantial portions of the software. This license is permissive and allows users to utilize the code for both commercial and non-commercial purposes.

Please see the [LICENSE](LICENSE) file for more details.