import os
import csv

#set path to file
budget_csv=os.path.join("Resources/budget_data.csv")

total_months = 0
net_total_amount = 0
Data = []
average_change_list = []
max_profit_list = []
min_profit = []

#open csv - see 1:59:38 lesson 3.2
with open(budget_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    print(csv_reader)
    #reads header row
    csv_header = next(csv_reader)
    
#looping through and add number of months to data list
    for row in csv_reader:
        total_months = total_months + 1
        Data.append(row[1])


#net total 
        net_total_amount = net_total_amount + int(row[1])
        # print(net_total_amount)

#months total
    i = 1 
    for i in range(1, len(Data)):
        # print(i)

# #average change
        average_change_list.append(int(Data[i])-int(Data[i-1]))
        print(average_change_list)

    avg = round(sum(average_change_list)/len(average_change_list),2)
    print(avg)
        
#greatest increase in profits
    # for row in csv_reader
    # x = 1 
    # for x in range(1, len(Data)):
    #     max_profit_list.append(int(Data[i])-int(Data[i-1]))
    #     print(max_profit_list)


#greatest decrease in profits
   

    print("Financial Analysis")
    print("------------------------")
    print("Total Months: " + str(total_months))
    print("Total: " + "$" +str(net_total_amount))
    print("Average Change: " + "$" + str(avg))
    # print("Greatest Increase in Profits: " + str(max_profit))
    # print("Greatest Decrease in Profits: " + str(min_profit))