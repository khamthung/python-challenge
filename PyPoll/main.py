import os
import csv

csvpath = os.path.join("..", "PyPoll","Resources", "election_data.csv")

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    firstrow = True
    secondrow = False
    names_list =[]
    votes_list =[]
    total_votes =0
    max_vote = 0
    winner_name=""
    for row in csvreader:
        if firstrow:
            firstrow = False
            secondrow = True
        elif secondrow:
            names_list.append(row[2])
            votes_list.append(1)
            total_votes +=1
            secondrow = False
        else:
            total_votes +=1
            for name in names_list:
                if name != row[2]:
                    found_new_name = True
                else:
                    votes_list[names_list.index(name)] = votes_list[names_list.index(name)]+1
                    found_new_name = False
                    break
            
            if found_new_name == True:
                names_list.append(row[2])
                votes_list.append(1)

print("\n\nElection Results\n-----------------------------------")
print(f'Total Votes: {total_votes}\n-----------------------------------')
for vote in votes_list:
    if vote > max_vote:
        max_vote = vote
        winner_name = names_list[votes_list.index(vote)]
    votes_percent = "{:.3f}".format(vote*100/total_votes)
    print(f'{names_list[votes_list.index(vote)]}: {votes_percent}% ({vote})')
print(f'-----------------------------------')
print(f'Winner: {winner_name}')
print(f'-----------------------------------\n\n')

output_txt_file = open("pypoll_output.txt","w+")
output_txt_file.write("Election Results\n-----------------------------------\n")
output_txt_file.write(f'Total Votes: {total_votes}\n-----------------------------------\n')
for vote in votes_list:
    output_txt_file.write(f'{names_list[votes_list.index(vote)]}: {votes_percent}% ({vote})\n')
output_txt_file.write(f'-----------------------------------\n')
output_txt_file.write(f'Winner: {winner_name}\n')
output_txt_file.write(f'-----------------------------------\n\n')