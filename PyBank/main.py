# Dependencies
import csv
import os

# Files to load and output (Remember to change these)
file_to_load = os.path.join("Resources", "budget_data.csv")

# Track various financial parameters
total_months = 0
total_profit_loss=0
monthly_change= 0
total_average_change=0
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Read the header row
    header = next(reader)

    for row in reader:
        total_months+=1
        monthly_change=int(row[1])
        total_profit_loss=total_profit_loss+monthly_change
        total_average_change=int(row[1])
    # print(total_profit_loss)

print(total_months)
print(total_profit_loss)
print(total_average_change)
