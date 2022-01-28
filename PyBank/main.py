import os
import csv

#set path to file
budget_csv=os.path.join("Resources", "budget_data.csv")

total_months = 0
net_total_amount = 0
average_change_list = []
max_profit = []
min_profit = []

#open csv - see 1:59:38 lesson 3.2
with open(budget_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    print(csv_reader)
    #reads header row
    csv_header = next(csv_reader)
    
#looping through and counting number of months 
    for row in csv_reader:

        total_months = total_months + 1

#net total 
        net_total_amount = net_total_amount + int(row[1])


#average change
        #average_change = round(int(net_total_amount) / int(total_months),2)
        
#greatest increase in profits
    # for row in csv_reader

#greatest decrease in profits
   

    print("Financial Analysis")
    print("------------------------")
    print("Total Months: " + str(total_months))
    print("Total: " + "$" +str(net_total_amount))
    # print("Average Change: " + "$" + str(average_change_list))
    # print("Greatest Increase in Profits: " + str(max_profit))
    # print("Greatest Decrease in Profits: " + str(min_profit))
