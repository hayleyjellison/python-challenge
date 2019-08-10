import csv
import os

csv_path = os.path.join("Resources","election_data.csv")

candidates = []
with open(csv_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    voter_count = 0
    csv_header = next(csvfile)
    for row in csvreader:
        candidates.append(row[2])
        voter_count = voter_count + 1

cand_names = []
def unique(list):
    for row in list:
        if row not in cand_names:
            cand_names.append(row)
    return cand_names

candy = unique(candidates)


khan_votes = candidates.count("Khan")
correy_votes = candidates.count("Correy")
li_votes = candidates.count("Li")
otooley_votes = candidates.count("O'Tooley")
votes = [int(khan_votes),int(correy_votes),int(li_votes),int(otooley_votes)]
clean = list(zip(candy,votes))
winner = [win for win in clean if win[1] == max(votes)]


# print(khan_votes)
# print(correy_votes)
# print(li_votes)
# print(otooley_votes)


khan_per = (khan_votes/voter_count)*100
correy_per = (correy_votes/voter_count)*100
li_per = (li_votes/voter_count)*100
otooley_per = (otooley_votes/voter_count)*100

with open("PyPoll.txt","w") as outfile:
    outfile.write("Election Results \n")
    outfile.write("---------------------- \n")
    outfile.write(f"Total Votes: {voter_count}\n")
    outfile.write("---------------------- \n")
    outfile.write(f"Khan: {str(round(khan_per,2))}% ({khan_votes} votes) \n")
    outfile.write(f"Correy: {str(round(correy_per,2))}% ({correy_votes} votes)\n")
    outfile.write(f"Li: {str(round(li_per,2))}% ({li_votes} votes)\n")
    outfile.write(f"O'Tooley: {str(round(otooley_per,2))}% ({otooley_votes} votes) \n")
    outfile.write("---------------------- \n")
    outfile.write(f"Winner: {winner[0][0]} \n")

print("Election Results \n")
print("---------------------- \n")
print(f"Total Votes: {voter_count}\n")
print("---------------------- \n")
print(f"Khan: {str(round(khan_per,2))}% ({khan_votes} votes) \n")
print(f"Correy: {str(round(correy_per,2))}% ({correy_votes} votes) \n")
print(f"Li: {str(round(li_per,2))}% ({li_votes} votes) \n")
print(f"O'Tooley: {str(round(otooley_per,2))}% ({otooley_votes} votes)\n")
print("---------------------- \n")
print(f"Winner: {winner[0][0]} \n")






