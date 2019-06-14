#import dependencies
import csv
import os

#initialize variables
file_path = os.path.join("Resources", "budget_data.csv")
month_counter = 0
max_profit_diff = 0
min_profit_diff = 0
max_date = ""
min_date = ""
profits = []
profit_diff = []
dates = []

#open csv file to begin processing
with open(file_path, "r") as f:
    reader = csv.reader(f)
    next(reader) #skip the header row
    for row in reader:  #read the rows to calculate total months and populate lists
        month_counter += 1     
        profits.append(int(row[1]))
        dates.append(row[0])             
    
    #create list of difference in profits to get max, min and average
    diff_profits_list = list(zip(profits, profits[1:]))        
    for x,y in diff_profits_list:
        profit_diff.append(y - x)

    for value in profit_diff:    
        current_profit_diff = value
        if current_profit_diff < min_profit_diff:  
            min_profit_diff = current_profit_diff
        if current_profit_diff > max_profit_diff:  
            max_profit_diff = current_profit_diff     
    
    max_date = dates[profit_diff.index(max_profit_diff) + 1]
    print(max_date)
    min_date = dates[profit_diff.index(min_profit_diff) + 1]
    #Display results in terminal
    print("Financial Analysis")
    print("-" * 30)
    print(f"Total Months: {month_counter}")
    print(f"Total: ${sum(profits)}")
    print(f"Average Change: ${sum(profit_diff) / len(profit_diff):.2f}")
    print(f"Greatest Increase in Profits: {max_date} (${max(profit_diff)})")
    print(f"Greatest Decrease in Profits: {min_date} (${min(profit_diff)})")

    #write results to a text file
    with open('profit_summary.txt', 'w') as f:
        f.write("Financial Analysis \n")
        f.write("---------------------------\n")
        f.write(f"Total Months: {month_counter} \n")
        f.write(f"Total: ${sum(profits)} \n")
        f.write(f"Average Change: ${sum(profit_diff) / len(profit_diff):.2f} \n")
        f.write(f"Greatest Increase in Profits: {max_date} (${max(profit_diff)}) \n")
        f.write(f"Greatest Decrease in Profits: {min_date} (${min(profit_diff)} \n")
    

