# Modules
import os
import csv

# Set path for file
election_csv=os.path.join("Resources", "election_data.csv")

# Variables
total_votes = 0
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0

# Open csv - see 1:59:38 lesson 3.2
with open(election_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    # print(csv_reader)
    # Reads header row
    csv_header = next(csv_reader)
    # print(csv_header)
   
# Loop through csv and count number of votes 
    for row in csv_reader:
        #total votes
        total_votes = total_votes + 1

# Votes for each candidate
        if row[2] == "Khan":
            khan_votes = khan_votes + 1
        elif row[2] == "Correy":
            correy_votes = correy_votes + 1
        elif row[2] =="Li":
            li_votes = li_votes + 1
        elif row[2] == "O'Tooley":
            otooley_votes = otooley_votes + 1
        
# Percent of votes each candidate won
    khan_percent = round((khan_votes/total_votes)*100,2)
    correy_percent = round((correy_votes/total_votes)*100,2)
    li_percent = round((li_votes/total_votes)*100,2)
    otooley_percent = round((otooley_votes/total_votes)*100,2)

# Determine winner
    if khan_votes > correy_votes and li_votes and otooley_votes:
        winner = "Khan"
    elif correy_votes > khan_votes and li_votes and otooley_votes:
        winner = "Correy"
    elif li_votes > khan_votes and correy_votes and otooley_votes:
        winner = "Li"
    else:
        winner = "O'Tooley"

# Analysis
    print(f"Election Results")
    print(f"----------------------------------")
    print(f"Total Votes: {total_votes}")
    print(f"----------------------------------")
    print(f"Khan: {khan_percent}% ({khan_votes})")
    print(f"Correy: {correy_percent}% ({correy_votes})")
    print(f"Li: {li_percent}% ({li_votes})")
    print(f"O'Tooley: {otooley_percent}% ({otooley_votes})")
    print(f"----------------------------------")
    print(f"Winner: {winner}")
    print(f"----------------------------------")


# Export to csv
# Reference: https://www.pythontutorial.net/python-basics/python-write-text-file/
# Reference: https://stackoverflow.com/questions/11497376/how-do-i-specify-new-lines-on-python-when-writing-on-files 
analysis = open("election.txt","w")
analysis.write("""
Election Results
----------------------------------
Total Votes: 3521001
----------------------------------
Khan: 63.0% (2218231)
Correy: 20.0% (704200)
Li: 14.0% (492940)
O'Tooley: 3.0% (105630)
----------------------------------
Winner: Khan
----------------------------------""")
