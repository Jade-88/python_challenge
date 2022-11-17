# Dependencies
import csv
import os

# Files to load and output (Remember to change these)
file_to_load = os.path.join("Resources", "election_data.csv")

# Track various financial parameters
total_votes = 0

with open(file_to_load) as election_result:
    reader = csv.reader(election_result)

    # Read the header row
    header = next(reader)

    for row in reader:
        total_votes+=1
        total_candidates=(int(row[1]))
        total_votes+=(int(row[0]))

print(total_votes)
print(total_candidates)
# Complete list of candidaates
file_to_load = os.path.join("Resources", "election_data.csv")

with open(file_to_load) as total_list_of_candidates:
    reader = csv.reader(total_list_of_candidates)

