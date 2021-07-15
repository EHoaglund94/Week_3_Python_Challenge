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

