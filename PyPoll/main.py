import csv
import os

file_path = os.path.join("Resources", "election_data.csv")

count = 0
max_votes = 0
election_results = {}

with open(file_path, "r") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        count += 1
        candidate = row[2]
        if candidate in election_results:
            election_results[candidate] += 1 
        else:
            election_results[candidate] = 1


    print("Election Results")
    print("-" * 30)
    print(f"Total Votes: {count}")
    print("-" * 30)
    for key in election_results:
        print(f"{key}: {(election_results[key] / count * 100):.3f}% ({election_results[key]})")
        if election_results[key] > max_votes:
            max_votes = election_results[key]
            winner = key
    print("-" * 30)  
    print(f"Winner: {winner}")  



with open('election_results.txt', 'w') as f:
    f.write("Election Results \n")
    f.write("-------------------------\n")
    f.write(f"Total Votes: {count} \n")
    for key in election_results:
        f.write(f"{key}: {(election_results[key] / count * 100):.3f}% ({election_results[key]}) \n")
        if election_results[key] > max_votes:
            max_votes = election_results[key]
            winner = key
    f.write("-------------------------\n")  
    f.write(f"Winner: {winner} \n")
    f.write("-------------------------\n") 



