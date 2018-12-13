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
    firstline = True
  
    for row in csvreader:
        if firstline:
            firstline = False
        else:
            total_months +=1
            total_amount = total_amount + int(row[1])
            avg_change = total_amount/total_months
            if (int(row[1]) > int(greatest_inc) ):
                greatest_inc = row[1]
            if (int(row[1]) < int(greatest_dec) ):
                greatest_dec = row[1]

    print("\n\nFinancial Analysis\n-----------------------------------")
    print(f'Total Months: {total_months}')
    print(f'Total: {total_amount}')
    print(f'Average Change: {avg_change}')
    print(f'Greatest Increase in Profits: ${greatest_inc}')
    print(f'Greatest Increase in Profits: ${greatest_dec}\n\n')

    output_txt_file = open("output.txt","w+")
    output_txt_file.write("Financial Analysis\n---------------------------------")
    output_txt_file.write(f'\nTotal Months: {total_months}')
    output_txt_file.write(f'\nTotal: {total_amount}')
    output_txt_file.write(f'\nAverage Change: {avg_change}')
    output_txt_file.write(f'\nGreatest Increase in Profits: ${greatest_inc}')
    output_txt_file.write(f'\nGreatest Increase in Profits: ${greatest_dec}')
