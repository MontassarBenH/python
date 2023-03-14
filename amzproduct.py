import requests
from bs4 import BeautifulSoup
import time
import smtplib


# Change this to the URL of the product you want to monitor
url = 'https://www.amazon.de/Viribus-Conversion-Electric-Bicycle-Pedelec/dp/B0B8D34D86'

# Fetch the initial price
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
price = float(soup.find('span', {'class': 'a-price-whole'}).text)

def send_email(subject, body):
    sender_email = 'example@gmail.com'
    sender_password = '12345'
    recipient_email = 'recipient@gmail.com'

    message = f'Subject: {subject}\n\n{body}'

    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.login(sender_email, sender_password)
        smtp.sendmail(sender_email, recipient_email, message)


# Monitor the price
while True:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    new_price = float(soup.find('span', {'class': 'a-price-whole'}).text)
    
    if new_price != price:
        print('Price changed!')
        send_email('Amazon price changed!', 'The price of the product has changed.')
        break
    
    time.sleep(86400 )  # Wait for 24 hour before checking again
    
