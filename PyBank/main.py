# Modules
import os
import csv

# Set path for file
budget_csv=os.path.join("Resources/budget_data.csv")

total_months = 0
net_total_amount = 0
Data = []
average_change = []

# Open csv - see 1:59:38 lesson 3.2
with open(budget_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    print(csv_reader)
    # Reads header row first
    csv_header = next(csv_reader)
    
# Loop through and add number of months to data list
    for row in csv_reader:
        total_months = total_months + 1
        Data.append(row[1])

# Net total 
        net_total_amount = net_total_amount + int(row[1])
        # print(net_total_amount)

# Months total
    i = 1 
    for i in range(1, len(Data)):
        # print(i)

# Average change - current row minue previous row
        average_change.append(int(Data[i])-int(Data[i-1]))
        # print(average_change_list)

    avg = round(sum(average_change)/len(average_change),2)
    # print(avg)
        
# Greatest increase in profits
    max_profit = max(average_change)
    # print(max_profit)

# Greatest decrease in profits
    min_profit = min(average_change)
    # print(max_profit)
   
# Analysis
    print("Financial Analysis")
    print("------------------------")
    print("Total Months: " + str(total_months))
    print("Total: " + "$" +str(net_total_amount))
    print("Average Change: " + "$" + str(avg))
    print("Greatest Increase in Profits: " + "$" + str(max_profit))
    print("Greatest Decrease in Profits: " + "$" + str(min_profit))

# Export to csv
# Reference: https://www.pythontutorial.net/python-basics/python-write-text-file/
# Reference: https://stackoverflow.com/questions/11497376/how-do-i-specify-new-lines-on-python-when-writing-on-files 
analysis = open("budget.txt","w")
analysis.write("""
Financial Analysis
----------------------------------
Total Months: 86
Total: $38382578
Average Change: $-2315.12
Greatest Increase in Profits: $1926159
Greatest Decrease in Profits: $-2196167 """)