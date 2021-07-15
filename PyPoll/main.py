import os
import csv

poll_csv = os.path.join('Resources','election_data.csv')

#Set variables
voter_id = []
candidates = []
candidate_votes = {}
winner_vote = 0



with open (poll_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    header = next(csvfile) 


    #Loop through CSV file to count number of voters, candidates, and votes for candidates
    for row in csvreader:
        candidate = row[2]
        voter_id.append(row[0])
        if candidate not in candidates:
            candidates.append(candidate)
            candidate_votes[candidate] = 1
        else:
            candidate_votes[candidate] += 1


#Summary data calculations
total_votes = len(voter_id)

candidate_percentage = {candidate : candidate_votes[candidate]/total_votes\
                        for candidate in candidates}
for item in candidate_percentage.items():
    if item[1] > winner_vote: 
        winner_vote = item[1]
        winner = item[0]







    







