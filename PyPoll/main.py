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
def inc_vote(vote_position): # increment the vote for the current candidate
    global votes
    votes[vote_position] = votes[vote_position] + 1

def calc_percentages(index): #calculate the percentages for each candidate
    global total_votes
    global votes
    global percentages
    percentages[index] = 100 * votes[index] / total_votes
    percentages[index] = percentages[index]

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast
winner = "" # Placeholder for the name of the winner

delay = 0 # delay value

# Define lists and dictionaries to track candidate names and vote counts
candidate_list = []
votes = [0,0,0]
percentages = [0,0,0]

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
        if candidate_name in candidate_list:
            x=0
        else:
            candidate_list.append(row[2])

        # Add a vote to the candidate's count
        if row[2] == candidate_list[0]: #If current row CANDIDATE = First candidate in list
            inc_vote(0)
        elif row[2] == candidate_list[1]: #If current row CANDIDATE = Second candidate in list
            inc_vote(1)
        elif row[2] == candidate_list[2]: #If current row CANDIDATE = Second candidate in list
            inc_vote(2)

    # Loop through the candidates to determine vote percentages and identify the winner
    for candidate in candidate_list:
        index = candidate_list.index(candidate)
        # Get the vote count and calculate the percentage
        calc_percentages(index)

        # Update the winning candidate if this one has more votes
        if index == 0:
            most_votes = votes[index]
            winner = candidate_list[index]

        if votes[index] > most_votes:
            winner = candidate_list[index]

# Save the winning candidate output to the text file
# Generate and print the winning candidate output
output = f'''
Election Results
-------------------------------------
Total Votes: {total_votes:,}
-------------------------------------
{candidate_list[0]}: {percentages[0]:,.3f}% ({votes[0]:,})
{candidate_list[1]}: {percentages[1]:,.3f}% ({votes[1]:,})
{candidate_list[2]}: {percentages[2]:,.3f}% ({votes[2]:,})
-------------------------------------
Winner: {winner}
-------------------------------------
'''

print(output)

# Open a text file to save the output
with open(file_to_output, "w") as txt_file:

    # Write results to text file
    txt_file.write(output)