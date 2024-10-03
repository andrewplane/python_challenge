# -*- coding: UTF-8 -*-
'''
Module 3 Challenge
python: PyBank
Andrew Lane
Oct 2, 2024
'''

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join('Resources', 'budget_data.csv')  # Input file path
file_to_output = os.path.join('analysis', 'budget_analysis.txt')  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0
total_changes = 0
previous_row_net = 0

# Add more variables to track other necessary financial data
avg_change = 0
greatest_inc = ['date', 0] #[date, amt]
greatest_dec = ['date', 0] #[date, amt]

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    # Extract first row to avoid appending to net_change_list
    header = next(reader)

    # Process each row of data
    for row in reader:
        
        # Track the total months and net change
        # Track the total months
        total_months = total_months + 1

        # Track the net change
        total_net = int(row[1]) + total_net
        if previous_row_net != 0:
            total_changes = total_changes + int(row[1]) - previous_row_net

        # Calculate the greatest increase in profits (month and amount)
        current_change = int(row[1]) - previous_row_net
        if current_change > int(greatest_inc[1]):
            greatest_inc = [row[0], current_change]

        # Calculate the greatest decrease in losses (month and amount)
        if current_change < int(greatest_dec[1]):
            greatest_dec = [row[0], current_change]

        previous_row_net = int(row[1]) # Adv previous net

# Calculate the average net change across the months
avg_change = total_changes / (total_months - 1)
avg_change = avg_change.__round__(2)

# Generate the output summary
output = f'''
Financial Analysis
--------------------------------
Total Months: {total_months}
Total: ${total_net:,.2f}
Average Change: {avg_change:,.2f}
Greatest Increase in Profits: {greatest_inc[0]} (${int(greatest_inc[1]):,.2f})
Greatest Decrease in Profits: {greatest_dec[0]} (${int(greatest_dec[1]):,.2f})
'''

# Print the output
print(output)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)