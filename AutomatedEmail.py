import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# SMTP server configuration
smtp_server = 'smtp.example.com'  # Replace with your SMTP server address
sender_email = 'your_email@example.com'  # Sender's email address
receiver_email = 'recipient@example.com'  # Recipient's email address
password = 'your_password'  # Sender's email password

# Create a MIMEMultipart message object
message = MIMEMultipart()
message['From'] = sender_email
message['To'] = receiver_email
message['Subject'] = 'Sample Email Subject'

# Email body
body = 'This is a sample email message.'
message.attach(MIMEText(body, 'plain'))

# Connect to the SMTP server
with smtplib.SMTP(smtp_server, 587) as server:
    # Start TLS encryption
    server.starttls()
    # Log in to the SMTP server
    server.login(sender_email, password)
    # Send the email
    server.sendmail(sender_email, receiver_email, message.as_string())
