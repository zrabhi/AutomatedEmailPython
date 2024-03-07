# Python Email Sender

This Python script demonstrates how to send an email using the Simple Mail Transfer Protocol (SMTP) in Python.

## Requirements

- Python 3.x

## Setup

1. Ensure you have a valid SMTP server address, sender email address, recipient email address, and sender email password.
2. Replace the placeholder values in the script with your actual SMTP server address, sender email address, recipient email address, and sender email password.

## How it Works

1. **SMTP Configuration**: Specify the SMTP server address, sender email address, recipient email address, and sender email password.

2. **Create Email Message**: Create a `MIMEMultipart` message object to compose the email message.

3. **Compose Email**: Set the sender, recipient, subject, and body of the email message.

4. **Connect to SMTP Server**: Establish a connection to the SMTP server.

5. **Start TLS Encryption**: Start TLS encryption for secure communication with the SMTP server.

6. **Login to SMTP Server**: Log in to the SMTP server using the sender's email address and password.

7. **Send Email**: Send the email message using the SMTP server.

## Usage

1. Clone or download the script.
2. Replace the placeholder values in the script with your actual SMTP server address, sender email address, recipient email address, and sender email password.
3. Run the script using Python.
4. Check the recipient email inbox to verify if the email was successfully sent.

## Important Note

- Ensure you have the necessary permissions to access the SMTP server and send emails using the provided sender email address.
- Keep your sender email password secure and do not share it publicly.

## Disclaimer

- Use this script responsibly and in accordance with your organization's email policies and guidelines.
