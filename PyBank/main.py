import os
import csv

csvpath = os.path.join("..", "PyBank","Resources", "budget_data.csv")

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    total_months=0
    total_amount=0
    avg_change=0
    greatest_inc=0
    greatest_dec=0
    firstrow = True
    to_sum_changes_firstmonth = True
    previous_month_amount =0
    sum_changes =0
  
    for row in csvreader:
       
        if firstrow:
            firstrow = False
        else:
            total_months +=1
            total_amount = total_amount + int(row[1])
            
            if to_sum_changes_firstmonth:
                previous_month_amount = int(row[1])
                to_sum_changes_firstmonth = False
            else:
                sum_changes = sum_changes+(int(row[1])-previous_month_amount)
                previous_month_amount = int(row[1])
                avg_change = "{:.2f}".format(sum_changes/(total_months-1))
            
            if (int(row[1]) > int(greatest_inc) ):
                greatest_inc = row[1]
                greatest_inc_date = row[0]
            if (int(row[1]) < int(greatest_dec) ):
                greatest_dec = row[1]
                greatest_dec_date = row[0]

    print("\n\nFinancial Analysis\n-----------------------------------")
    print(f'Total Months: {total_months}')
    print(f'Total: ${total_amount}')
    print(f'Average Change: ${avg_change}')
    print(f'Greatest Increase in Profits: {greatest_inc_date} (${greatest_inc})')
    print(f'Greatest Increase in Profits: {greatest_dec_date} (${greatest_dec})\n\n')

    output_txt_file = open("pybank_output.txt","w+")
    output_txt_file.write("Financial Analysis\n---------------------------------")
    output_txt_file.write(f'\nTotal Months: {total_months}')
    output_txt_file.write(f'\nTotal: ${total_amount}')
    output_txt_file.write(f'\nAverage Change: ${avg_change}')
    output_txt_file.write(f'\nGreatest Increase in Profits: {greatest_inc_date} (${greatest_inc})')
    output_txt_file.write(f'\nGreatest Increase in Profits: {greatest_dec_date} (${greatest_dec})')
