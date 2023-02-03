# my_email, password, and to_addrs are using variables from a .env file, hence why os and dotenv are imported

import smtplib, datetime, random, os
from dotenv import load_dotenv

load_dotenv()

my_email = os.getenv("send_email")
recieve_email = os.getenv("recieve_email")
password = os.getenv("app_pass")
now = datetime.datetime.now()
day_of_week = now.weekday()

def choosequote():
    with open("quotes.txt") as quotes:
        lines = [line for line in quotes]
        return random.choice(lines)

def sendmail():
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(
            from_addr = my_email, 
            to_addrs = recieve_email, 
            msg = f"Subject:Quote for today!\n\n{choosequote()}"
        )

if day_of_week == 4:
    sendmail()