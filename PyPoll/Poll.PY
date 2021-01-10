import csv 
import os
path = os.path.join("Resources","election_data.csv")

total_votes = 0
Khan = 0
Correy = 0
Li = 0
O_Tooley = 0
    

with open(path) as Data:
    reader = csv.reader(Data)
    header = next(reader)
    for row in reader:
        total_votes+=1

        if row[2] == "Khan":
            Khan += 1 
        
        if row[2] == "Correy":
            Correy += 1

        if row[2] == "Li":
            Li += 1

        if row[2] == "O'Tooley":
            O_Tooley += 1


print(Khan)
print(Correy)
print(Li)
print(O_Tooley)
print(total_votes)

percentage_k = Khan / total_votes * 100
percentage_c = Correy / total_votes * 100
percentage_l = Li / total_votes * 100
percentage_t = O_Tooley / total_votes * 100

print(f"Khan: {percentage_k} ({Khan})")
print(f"Correy: {percentage_k} ({Correy})")
print(f"Li: {percentage_k} ({Li})")
print(f"O_Tooley: {percentage_k} ({O_Tooley,2})")

print("Election Results")
print("--------------------------")
print(f"Total Votes: {str(total_votes)}")
print("--------------------------")
print()
