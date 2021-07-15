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

#Put Summary Data into a list
summary_data = []
line1 = 'Election Results'
line2 = '-' *25
line3 = (f'Total Votes: {total_votes}')
line4 = '-' *25

line5 = "{}: ".format(candidates[0]) + \
        '{:.1%} '.format(candidate_percentage[candidates[0]]) + \
        '({}) '.format(candidate_votes[candidates[0]])

line6 = "{}: ".format(candidates[1]) + \
        '{:.1%} '.format(candidate_percentage[candidates[1]]) + \
        '({}) '.format(candidate_votes[candidates[1]])

line7 = "{}: ".format(candidates[2]) + \
        '{:.1%} '.format(candidate_percentage[candidates[2]]) + \
        '({}) '.format(candidate_votes[candidates[2]])

line8=  "{}: ".format(candidates[3]) + \
        '{:.1%} '.format(candidate_percentage[candidates[3]]) + \
        '({}) '.format(candidate_votes[candidates[3]])

line9 = '-' *25
line10 = (f'Winner: {winner}')
line11 = '-' *25
summary_data.extend([line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11])

#print to terminal
for line in summary_data:
    print(line)












    







