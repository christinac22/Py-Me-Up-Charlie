import os
import csv

election_csv=os.path.join("Resources", "election_data.csv")

#variables
total_votes = 0
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0

#open csv - see 1:59:38 lesson 3.2
with open(election_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    # print(csv_reader)
    #reads header row
    csv_header = next(csv_reader)
    # print(csv_header)
   
#looping through csv and counting number of votes by row
    for row in csv_reader:
        #total votes
        total_votes = total_votes + 1

#votes for each candidate
        if row[2] == "Khan":
            khan_votes = khan_votes + 1
        elif row[2] == "Correy":
            correy_votes = correy_votes + 1
        elif row[2] =="Li":
            li_votes = li_votes + 1
        elif row[2] == "O'Tooley":
            otooley_votes = otooley_votes + 1
        
#percent of votes each candidate won
    khan_percent = round((khan_votes/total_votes)*100,2)
    correy_percent = round((correy_votes/total_votes)*100,2)
    li_percent = round((li_votes/total_votes)*100,2)
    otooley_percent = round((otooley_votes/total_votes)*100,2)

#determine winner


    #Analysis
    print(f"Election Results")
    print(f"----------------------------------")
    print(f"Total Votes: {total_votes}")
    print(f"----------------------------------")
    print(f"Khan: {khan_percent}% ({khan_votes})")
    print(f"Correy: {correy_percent}% ({correy_votes})")
    print(f"Li: {li_percent}% ({li_votes})")
    print(f"O'Tooley: {otooley_percent}% ({otooley_votes})")

