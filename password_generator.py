# importing datetime, holidays and assign key datetime variables

from datetime import datetime

# in terminal: python3 -m pip install https://packaging.python.org/en/
# latest/tutorials/installing-packages/#use-pip-for-installing

import holidays

import string

import secrets  # can also use random however not cryptographically secure

now = datetime.now()
hour = now.hour
year = now.year
d = datetime.date(now)
day = now.strftime("%A")
# checking the time of day
if hour < 12:
    greeting = "Good morning"
elif hour < 18:
    greeting = "Good afternoon"
else:
    greeting = "Good evening"
# system greets the user
print(greeting, "\n")
print("Welcome python password generator", "\n")
# password type from user
normal = string.ascii_letters + string.digits + string.punctuation
num_only = string.digits
no_special_characters = string.ascii_letters + string.digits
password_type = [normal, num_only, no_special_characters]
password_id = int(input("Please enter a password type (normal = 0; number only \
= 1; and no special\n characters = 2): "))
print(" ")
# password length from user
length = int(input("Enter password length: "))
print(" ")
# picking random characters from the list
password = "".join(secrets.choice(password_type[password_id]) \
                   for i in range(length))  # i is a temp variable
print("Your password is:", password, "\n")
# the system wishes the user a good holiday, weekend or day dependent on
# today's date
check_for_holiday = d in holidays.England()
check_for_weekend = day == "Sunday" or "Saturday"
if check_for_holiday == True:
    day_type = holidays.England().get(d)
elif check_for_weekend == True:
    day_type = "weekend"
else:
    day_type = "day"
print("Thank you for using the password generator", "\n")
print("Have a good", day_type + "!")
