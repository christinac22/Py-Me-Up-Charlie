import os
import csv

election_csv=os.path.join("Resources", "election_data.csv")

total_votes = 0


#open csv - see 1:59:38 lesson 3.2
with open(election_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    print(csv_reader)
    #reads header row
    csv_header = next(csv_reader)
    #print(csv_header)
   
#looping through csv and counting number of votes by row
    for row in csv_reader:
        #total votes
        total_votes = total_votes + 1

#votes for each candidate
# for candidate in candidates:

          
#percent of votes each candidate won

#determine winner


    #Analysis
    print("Election Results")
    print("------------------------")
    print("Total Votes: " + str(total_votes))
