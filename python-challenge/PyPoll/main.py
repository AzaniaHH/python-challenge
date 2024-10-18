import os
import csv

file_path = '/Users/zan/Desktop/python-challenge/python-challenge/PyPoll/election_data.csv'

total_votes = 0
candidate_votes = {}

with open(file_path, mode='r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader) 

    for row in csv_reader:
        total_votes += 1
        candidate = row[2]
        
        if candidate not in candidate_votes:
            candidate_votes[candidate] = 0
        
        candidate_votes[candidate] += 1

winner = max(candidate_votes, key=candidate_votes.get)

print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

for candidate, votes in candidate_votes.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")

print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

text_file_path = '/Users/zan/Desktop/python-challenge/python-challenge/PyPoll/election_results.txt'

with open(text_file_path, mode='w') as text_file:
    text_file.write("Election Results\n")
    text_file.write("-------------------------\n")
    text_file.write(f"Total Votes: {total_votes}\n")
    text_file.write("-------------------------\n")

    for candidate, votes in candidate_votes.items():
        percentage = (votes / total_votes) * 100
        text_file.write(f"{candidate}: {percentage:.3f}% ({votes})\n")

    text_file.write("-------------------------\n")
    text_file.write(f"Winner: {winner}\n")
    text_file.write("-------------------------\n")
