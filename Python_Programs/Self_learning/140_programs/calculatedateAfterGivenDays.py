# Program to calculate future date using timedelta

import datetime

days = int(input("Enter number of days to add: "))

today = datetime.date.today()
future_date = today + datetime.timedelta(days=days)

print("Future Date:", future_date)

#  Output:
# Enter number of days to add: 5
# Future Date: 2026-03-08