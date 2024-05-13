import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from constants import SENDER, PASSWORD, RECEIVER, GMAIL_HOST, GMAIL_PORT


def send_email(subject, body):
    """
    Send an email using SMTP protocol with Gmail's SMTP server.

    Args:
        subject (str): The subject line of the email.
        body (str): The HTML-formatted body of the email.

    Returns:
        bool: True if the email was sent successfully, otherwise False.

    Raises:
        Exception: If an error occurs during the email sending process.
    """
    # Create a MIMEMultipart message (Multipurpose Internet Mail Extensions)
    message = MIMEMultipart()

    # Set the sender, receiver, and subject of the email
    message['From'] = SENDER
    message['To'] = RECEIVER
    message['Subject'] = subject

    # Create a MIMEText object to represent the email body
    mimetext = MIMEText(body, 'html')

    # Attach the MIMEText object to the MIMEMultipart message
    message.attach(mimetext)

    try:
        # Establish connection with Gmail SMTP server using 'with' statement
        with smtplib.SMTP(GMAIL_HOST, GMAIL_PORT) as server:
            # Initiate connection with the server
            server.ehlo()

            # Initiate TLS encryption
            server.starttls()

            # Log in to the sender's email account
            server.login(SENDER, PASSWORD)

            # Send the email after converting the message MIMEMultipart object to string
            server.sendmail(SENDER, RECEIVER, message.as_string())

            return True
    except Exception as err:
        # Raise the caught exception for handling at a higher level
        raise err
