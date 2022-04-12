import datetime as dt
from smtplib import *
import random

# ENTER your login info here, recipient email, and smtp server for YOUR SENDING email:
MY_EMAIL = "YOUR EMAIL HERE"    
MY_PASSWORD = "YOUR EMAIL'S PASSWORD HERE"
RECIPIENT_EMAIL = "EMAIL YOU WISH TO SEND TO"
# Yahoo: smtp.mail.yahoo.com, Gmail: smtp.gmail.com  - If using other email provider, just search google for "smtp server"
EMAIL_SMTP = "smtp.mail.yahoo.com"
# Change to day you want email to send. Monday=0, Tuesday=1...Sunday=6
DAY_TO_SEND = 0

now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == DAY_TO_SEND:

    with open("quotes.txt", "r") as quotes:
        data = quotes.readlines()
        quote = random.choice(data)

    # Opening connection 
    with SMTP(EMAIL_SMTP) as connection:
        # Securing Connection
        connection.starttls()
        # Login in to email
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=RECIPIENT_EMAIL,
            # The content of email (Here is the random quote)
            msg=f"Subject:Motivational Quote\n\n{quote}"
        )
