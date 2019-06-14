import csv
import os

file_path = os.path.join("Resources", "budget_data.csv")
month_counter = 0
total_profit = 0
max_profit = 0
min_profit = 0
max_date = ""
min_date = ""

with open(file_path, "r") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        month_counter += 1
        profit = int(row[1])
        total_profit += profit
        if profit > max_profit:
            max_profit = profit
            max_date = row[0]
        if profit < min_profit:
            min_profit = profit
            min_date = row[0]
    
    print("Financial Analysis")
    print("-" * 30)
    print(f"Total Months: {month_counter}")
    print(f"Total: {total_profit}")
    print(f"Average Change: {total_profit / month_counter}")
    print(f"Greatest Increase in Profits: {max_date} ({max_profit})")
    print(f"Greatest Decrease in Profits: {min_date} ({min_profit})")

    with open('profit_summary.txt', 'w') as f:
        f.write("Financial Analysis \n")
        f.write("---------------------------\n")
        f.write(f"Total Months: {month_counter} \n")
        f.write(f"Total: {total_profit} \n")
        f.write(f"Average Change: {total_profit / month_counter} \n")
        f.write(f"Greatest Increase in Profits: {max_date} ({max_profit}) \n")
        f.write(f"Greatest Decrease in Profits: {min_date} ({min_profit}) \n")
    

