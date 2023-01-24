import os
import csv

#create the path to the file
PyPoll_path = os.path.join('Resources', 'election_data.csv')

total_votes = 0 #to be incremented by the sum of rows

candidates_options = [] #list of candidate options
candidate_votes = {} #dictionary to define key as the candidate and values the votes they receive

#for the final results of the overall voting
winning_candidate = ""
winning_count = 0

with open(PyPoll_path) as pollfile:
    reader = csv.DictReader(pollfile) #same as the pybank to avoing "next"

    for row in reader:
        total_votes = total_votes +1 #each row means one vote since the header is skipped

        candidate_name = row["Candidate"]

        if candidate_name not in candidates_options:
            candidates_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

poll_results = os.path.join('analysis', 'analysis.txt')

with open(poll_results, "w") as results_file:
    
    poll_results =(
        f'\n\nElection Results\n'
        f'---------------------------\n'
        f'Total Votes: {total_votes}\n'
        f'---------------------------\n')

    print(poll_results)
    results_file.write(poll_results)

    for candidate in candidate_votes:
        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes) / float(total_votes) * 100

        if votes > winning_count:
            winning_count = votes
            winning_candidate = candidate
        
        voter_output = f'{candidate}: {vote_percentage:.3}% {votes}\n'
        print(voter_output)
        #add each to the txt file
        results_file.write(voter_output)

    
    winning_candidate_summary = (
        f'-----------------------\n'
        f'Winner: {winning_candidate}\n'
        f'-----------------------\n'
    )
    print(winning_candidate_summary)
    results_file.write(winning_candidate_summary)
