import os
import csv

file_path = "PyBank/Resources/budget_data.csv"

total_months = 0
net_total = 0
previous_profit_loss = None
changes = []
dates = []

greatest_increase = {"date": "", "amount": float('-inf')}
greatest_decrease = {"date": "", "amount": float('inf')}

with open(file_path, mode='r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)

    for row in csv_reader:
        date, profit_loss = row[0], int(row[1])
        
        total_months += 1
        
        net_total += profit_loss

        if previous_profit_loss is not None:
            change = profit_loss - previous_profit_loss
            changes.append(change)
            dates.append(date)
            
            if change > greatest_increase["amount"]:
                greatest_increase = {"date": date, "amount": change}
            
            if change < greatest_decrease["amount"]:
                greatest_decrease = {"date": date, "amount": change}
        
        previous_profit_loss = profit_loss

average_change = sum(changes) / len(changes) if changes else 0

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})")
print(f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})")


    
