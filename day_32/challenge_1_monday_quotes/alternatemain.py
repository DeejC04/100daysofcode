# This is just a slightly modified version of main.py. Primary changes are in choosequote(), regarding the method a random quote is chosen

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
        allquotes = quotes.readlines()
        return random.choice(allquotes)

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

