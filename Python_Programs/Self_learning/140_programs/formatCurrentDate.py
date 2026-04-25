# Program to format current date

import datetime

today = datetime.datetime.now()

formatted = today.strftime("%d-%m-%Y")

print("Formatted Date:", formatted)

# Output:
# Formatted Date: 04-03-2026