# importing datetime and holidays
# may need to install holidays
# https://packaging.python.org/en/latest/tutorials/installing-packages/#use-pip-for-installing

from datetime import datetime
import holidays
import string
import secrets  # can also use random however not cryptographically secure

# assigning key datetime variables

now = datetime.now()
hour = now.hour
year = now.year
d = datetime.date(now)
day = now.strftime("%A")

# 24 h format time:

current_time = now.strftime("%H:%M:%S")

# date in abrivated month format:

current_date = now.strftime("%d %b %Y")

# checking the time of day

if hour < 12:
    greeting = "Good morning"
elif hour < 18:
    greeting = "Good afternoon"
else:
    greeting = "Good evening"

# system greets the user

print(greeting, "\n")
print("Welcome to python password generator", "\n")

# password types:

normal = string.ascii_letters + string.digits + string.punctuation
num_only = string.digits
no_special_characters = string.ascii_letters + string.digits

# creating list (called password_type) with each password type

password_type = [normal, num_only, no_special_characters]

# selecting from the list (password_type) with input from the user

password_id = int(input("Please enter a password type (normal = 0; number only = 1; and no special\n characters = 2): "))
print(" ")

# selecting a password length with input from the user

length = int(input("Enter password length: "))
print(" ")

# picking random characters, were the type of character is dictated by the selected password type:

password = "".join(secrets.choice(password_type[password_id]) for i in range(length))  # i is a temp variable

# naming what the password is for

password_for = input("What is the password for? ")

# desplaying the password and printing it to a .txt file named passowords:

with open("passwords.txt", "a") as external_file:
    print("\n", current_date, current_time, password_for, password, file=external_file)
    external_file.close()

print("Your password is:", password, "\n")

# the system wishes the user a good holiday, weekend or day dependent on today's date:

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
