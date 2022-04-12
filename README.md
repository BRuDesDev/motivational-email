# motivational-email
A program written in Python that sends an email once a week, containing a random motivational quote.  Uses datetime, random, and smtplib modules.


# Download and Setup
>$ git clone https://github.com/jaHSHuaBR/motivational-email.git
>
>$ cd motivational-email

# Open main.py to edit Constant
>$ sudo nano main.py

# Fill in the constants with correct info
MY_EMAIL = "your email to send from"

MY_PASSWORD = "password to login to your above email"

RECIPIENT_EMAIL = "email to send to"

EMAIL_SMTP = "the smtp host server for your email"  # yahoo = "smtp.mail.yahoo.com" | gmail = "smtp.gmail.com | hotmail = smtp.live.com | If using other provider, google to find smtp server

DAY_TO_SEND = "the day you want email to send. Monday=0, Tuesday=1...Sunday=6"

# Once you have filled in the variables to work properly, just run:
>$ python3 main.py
