import os
import csv

poll_csv = os.path.join('Resources','election_data.csv')

#Set variables
output_keys = ['Candidate', 'Number of Votes', 'Percentage of Votes']
voter_id = []
candidates = []
candidate_votes = {}



with open (poll_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    header = next(csvfile) 


    #Loop through CSV file to count number of voters, candidates, and votes for candidates
    for row in csvreader:
        candidate = row['Candidate']
        voter_id.append(row['Voter ID'])
        if candidate not in candidates:
            candidates.append(candidate)
            candidate_votes[candidate] = 1
        else:
            candidate_votes[candidate] += 1

    







