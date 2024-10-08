# -*- coding: UTF-8 -*-
'''
Module 3 Challenge
python: PyPoll
Andrew Lane
Oct 2, 2024
'''

# Import necessary modules
import csv
import os

# Define Functions
def create_vote_results(candidate_count, keys_list, candidate_votes, total_votes):
    lines = [] #store generated lines of text
    multi_line_string = "" #store multiline output
    
    i = 0
    while i < candidate_count: # Loop through the candidates
        name = keys_list[i] # store the name of the candidate for readability
        votes = candidate_votes[name]
        lines.append(f'{name}: {100*votes/total_votes:.3f}% ({votes:,})')
        i += 1

    # Join the lines into a single string with newline characters
    multi_line_string = "\n".join(lines)
    return multi_line_string

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast
winner = ["",0] # Placeholder for the name of the winner
candidate_count = 0 # Track number of candidates
delay = 0 # delay value

# Define lists and dictionaries to track candidate names and vote counts
candidate_list = [] # holds list of candidate names
candidate_votes = {} # holds candidate names and votes

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:

        # Print a loading indicator (for large datasets)
        delay = delay + 1
        if delay > 10000:
            print(". ", end="")
            delay = 0

        # Increment the total vote count for each row
        total_votes = total_votes + 1

        # Get the candidate's name from the row
        candidate_name = row[2]

        # If the candidate is not already in the candidate list, add them
        if candidate_name in candidate_votes:
            x=0
        else:
            # Increment Candidate Count
            candidate_count = candidate_count + 1
            # Create a new entry in the dictionary "Name": 0
            candidate_votes[row[2]] = 0 

        # Add a vote to the candidate's count
        candidate_votes[row[2]] = candidate_votes[row[2]] + 1
        
    # Loop through the candidates to determine vote percentages and identify the winner
    for candidate in candidate_votes:

        # Update the winning candidate if this one has more votes
        if candidate_votes[candidate] > winner[1]:
            # winner stores the name and the number of votes
            winner = [candidate, candidate_votes[candidate]]

keys_list = list(candidate_votes.keys())

# Save the winning candidate output to the text file

# Generate and print the winning candidate output

#Generate the top section of the output
output1 = f'''
Election Results
-------------------------------------
Total Votes: {total_votes:,}
-------------------------------------
'''

# Generate the middle section of the output (1 line per candidate)
output2 = create_vote_results(candidate_count, keys_list, candidate_votes, total_votes)

# Generate the bottom section of the output
output3 = f'''
-------------------------------------
Winner: {winner[0]}
-------------------------------------
'''

# Concatonate the outputs
output = output1 + output2 + output3

#Print the combined output
print(output)

# Open a text file to save the output
with open(file_to_output, "w") as txt_file:

    # Write results to text file
    txt_file.write(output)