import smtplib
import env
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from src.compare_prices import price_diff, last_price
from src.scrape_stock import price

smtp_server = env.SMTP_SERVER
smtp_port = env.SMTP_PORT
sender_email = env.SENDER_EMAIL
receiver_email = env.RECEIVER_EMAIL
password = env.EMAIL_PASSWORD

subject = 'Apple Stock Price Alert'
body = f'Current Apple stock price: ${price}\nPrice difference: ${price_diff if last_price else "N/A"}'

msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = subject
msg.attach(MIMEText(body, 'plain'))

with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, msg.as_string())

print('Email sent successfully.')
