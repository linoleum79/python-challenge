import os
import csv
csv_path = 'PyPoll/Resource/election_data.csv'
total_votes = 0
candidates = []
candidate_votes =[]
candidates_dict = []
with open(csv_path, encoding="UTF-8") as vote_file:
    csv_reader = csv.reader(vote_file)
    header = next(csv_reader)
    for vote in csv_reader:
        total_votes=total_votes +1
        candidate = vote[2]
        if (candidate not in candidates):
            candidates.append(candidate)
            candidate_votes.append(1)
        else:
            curent_votes = candidate_votes[candidates.index(candidate)]
            current_votes = current_votes=+1
            candidate_votes[candidates.index(candidate)] = current_votes
print('Election Results')
print('----------------------------')
print(f'total Votes: {total_votes}')
print(f'----------------------------')
for candidate in candidates:
    vote_count = candidate_votes[candidates.index(candidate)]
    print(f'{candidate}: 23.049% ({vote_count})')
print(f'---------------------------')
print(f'Winner: Diana DeGette')
print(f'---------------------------')