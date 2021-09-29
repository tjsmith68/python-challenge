import os 

vote_count = 0
candidate_count = 0

#Empty dictionary
candidates = {}

file = os.path.join('Resources','election_data.csv')

filedata = open(file,"r")

stillreading = True

# Dummy read to skip headings line

line = filedata.readline()

# Loop to read remaining data

first_row = True

while stillreading:
    line = filedata.readline()
    item = line.split(",")
    #If no new row, set loop exit condition
    if item[0] == "":
        stillreading = False
    else:
        #Only process if you read a new line
        item[2] = item[2].rstrip()
        vote_count = vote_count + 1  
        if first_row:
            #First candidate automatically gets added as a new item in the dictionary
            candidate_count = candidate_count + 1
            candidates[item[2]] = 1
            first_row = False
        else:
            candList = candidates.keys()
            if item[2] in candList:
                currVotes = candidates[item[2]] + 1
                candidates[item[2]] = currVotes
            else:
                candidate_count = candidate_count + 1
                candidates[item[2]] = 1


filedata.close()

# Output the Analysis to the terminal

print("Election Results")
print("---------------------------------------")
print(f"Total Votes: {vote_count}")
print("---------------------------------------")

highVotes = 0
winner = " "

candList = candidates.keys()
for name in candList:
    votes = candidates[name]
    percentV = round((votes * 100)/vote_count,3)
    print(f"{name}: {percentV}% ({votes})")
    if votes > highVotes:
        winner = name
        highVotes = votes

print("---------------------------------------")
print(f"Winner: {winner} ")
print("---------------------------------------")



outfile = os.path.join('Resources','Results.txt')

fileout = open(outfile,"w")

# Output the Analysis to a file

fileout.write("Election Results\n")
fileout.write("---------------------------------------\n")
fileout.write(f"Total Votes: {vote_count}\n")
fileout.write("---------------------------------------\n")

highVotes = 0
winner = " "

candList = candidates.keys()
for name in candList:
    votes = candidates[name]
    percentV = round((votes * 100)/vote_count,3)
    fileout.write(f"{name}: {percentV}% ({votes})\n")
    if votes > highVotes:
        winner = name
        highVotes = votes

fileout.write("---------------------------------------\n")
fileout.write(f"Winner: {winner} \n")
fileout.write("---------------------------------------\n")

fileout.close()