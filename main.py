import datetime as dt
import pandas as pd
import random
import smtplib

MY_EMAIL = "stuga718@gmail.com"
PASSWORD = "jjcrxzuvevlcxmfd"
GOOGLE_MAIL_SERVER = "smtp.gmail.com"

today = (dt.datetime.now().month, dt.datetime.now().day)
df = pd.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in df.iterrows()}

if today in birthdays_dict:
    # today is a tuple that's actually a key to retrieve values from the birthdays_dict.
    birthday_person = birthdays_dict[today]
    #  birthday_person is the entire row of data.
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP(GOOGLE_MAIL_SERVER) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=birthday_person["email"], msg=f"Subject:Happy Birthday"
                                                                                       f"\n\n{contents} ")
