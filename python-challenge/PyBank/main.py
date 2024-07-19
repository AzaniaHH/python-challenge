import os
import csv

file_path = "PyBank/Resources/budget_data.csv"

def count_first_column_values(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        first_column_values = [row[0] for row in reader]
        return len(first_column_values)

count = count_first_column_values(file_path)
print(f'Total Months: {count}')


    