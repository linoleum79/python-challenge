import os
import csv
csv_path = 'PyBank/Resource/budget_data.csv'
profit = []
monthly_changes = []
date = []

total_months = 0
total_profit = 0
total_change_profits = 0
initial_profit = 0

with open(csv_path,encoding="UTF-8") as bank_file:
    csvreader = csv.reader(bank_file, delimiter=",")
    csv_header = next(csvreader)
    for row in csvreader:
        total_months = total_months +1
        date.append(row[0])
        







print('Financial Analysis')
print('----------------------------')
print
print
print
print
print
