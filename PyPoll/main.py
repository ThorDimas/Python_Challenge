import os
import csv

#create the path to the file
PyPoll_path = os.path.join('Resources', 'election_data.csv')

total_votes = 0

candidates_options = []
candidate_votes = {}

winning_candidate = ""
winning_count = 0




with open(PyPoll_path) as pollfile:
    reader = csv.DictReader(pollfile)

    for row in reader:
        total_votes = total_votes +1

        candidate_name = row["Candidate"]

        if candidate_name not in candidates_options:
            candidates_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1
    
    print(
        f'\n\nElection Results\n'
        f'---------------------------\n'
        f'Total Votes: {total_votes}\n'
        f'---------------------------\n'

    )
    for candidate in candidate_votes:
        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes) / float(total_votes) * 100

        if votes > winning_count:
            winning_count = votes
            winning_candidate = candidate
        
        voter_output = f'{candidate}: {vote_percentage:.3}% {votes}\n'
        print(voter_output)
    
    winning_candidate_summary = (
        f'-----------------------\n'
        f'Winner: {winning_candidate}\n'
        f'-----------------------\n'
    )
    print(winning_candidate_summary)
