import smtplib
import random
import datetime as dt
import pandas

my_email = "YOUR EMAIL"
password = "YOUR PASSWORD"

now = dt.datetime.now()
current_month = now.month
current_day = now.day

birthdays = pandas.read_csv("birthdays.csv")

for month in birthdays.month:
    if month == current_month:
        for day in birthdays.day:
            if day == current_day:
                row = birthdays[birthdays.day == day]
                name_series = row.name
                name = name_series[0]
                letters = []
                with open("letter_templates/letter_1.txt", "r") as letter_file:
                    letters.append(letter_file.read())
                with open("letter_templates/letter_2.txt", "r") as letter_file:
                    letters.append(letter_file.read())
                with open("letter_templates/letter_3.txt", "r") as letter_file:
                    letters.append(letter_file.read())
                    
                letter = random.choice(letters)
                letter_with_name = letter.replace("[NAME]", name)

                with smtplib.SMTP("smtp.gmail.com") as connection:
                    connection.starttls()
                    connection.login(user=my_email, password=password)
                    connection.sendmail(from_addr=my_email,
                                        to_addrs="Your adress",
                                        msg=f"Subject:Happy Birthday! \n\n {letter_with_name}")





