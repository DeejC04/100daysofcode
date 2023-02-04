# extrahard variant. I did this with just some extra Googling. Not a fan of how repetitive it gets sometimes
# overall, not the most efficient code whatsoever (extremely inefficient actually). Needs work, but it does accomplish the goal

import smtplib, datetime, random, pandas, os
from dotenv import load_dotenv

load_dotenv()
n = 0
birthdays = pandas.read_csv("birthdays.csv")
month_day = birthdays[["month", "day"]]
today = datetime.datetime.now()
my_email = os.getenv("send_email")
recieve_email = birthdays["email"][n]
password = os.getenv("app_pass")

def sendmail():
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(
            from_addr = my_email, 
            to_addrs = recieve_email, 
            msg = f"Subject:Quote for today!\n\n{chooseletter()}"
        )

def chooseletter():
    global letternumber
    letternumber = str(random.randint(1, 3))
    with open(f"./letter_templates/letter_{letternumber}.txt") as letter:
        text = letter.read()
        text = text.replace("[NAME]", birthdays["name"][n])
        return text

for _ in month_day:
    day = today.day
    month = today.month
    if birthdays["month"][n] == month and birthdays["day"][n] == day:
        sendmail()
    n += 1