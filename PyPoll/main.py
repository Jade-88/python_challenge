# Dependencies
import csv
import os

# Files to load and output (Remember to change these)
file_to_load = os.path.join("Resources", "election_data.csv")

# Track various financial parameters
total_votes = 0
candidates = []
candidate_vote={}

with open(file_to_load) as election_result:
    reader = csv.reader(election_result)

    # Read the header row
    header = next(reader)

    for row in reader:
        total_votes+=1

        candidate_name=row[2]

        if candidate_name not in candidates:
            candidates.append(candidate_name)
            candidate_vote[candidate_name]=0
        
        candidate_vote[candidate_name]=candidate_vote[candidate_name]+1

        # total_candidates=(int(row[0]))
        # total_votes+=(int(row[0]))
        
print(total_votes)
print(candidates)
print(candidate_vote)


with open(file_to_write,'w') as output:
    output.write(Election_Result)
     # Read the header row
    
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
print(f"{candidates[0]}: {candidate_vote[candidates[0]]}")