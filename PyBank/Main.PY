import csv 
import os
path = os.path.join("Resources","budget_data.csv")

total_months = 0
total_profit = 0
changes = []
months = []


with open(path) as Data:
    reader = csv.reader(Data)
    header = next(reader)
    first_row = next(reader)
    total_months += 1
    total_profit += int(first_row[1])
    last_month = int(first_row[1])


    for row in reader:
        total_months = total_months + 1 
        total_profit = total_profit + int(row[1])
        difference = int(row[1]) - last_month
        last_month = int(row[1])
        changes.append(difference)
        months.append(row[0])


max_change = max(changes)
min_change = min(changes)

month_index = changes.index(max(changes))
max_month = months[month_index]

min_index = changes.index(min(changes))
min_month = months[min_index]
average = sum(changes) / len(changes)

output = os.path.join("analysis.txt")
with open(output,"w") as file: 

    print("Financial Analysis", file=file)
    print("------------------------", file=file)
    print("Total Months: " + str(total_months), file=file)
    print(f"Total Profit: ${total_profit}", file=file)

    print(f"Average Change: ${round(average,2)}", file=file)

    print(f"Greatest Increase: {max_month} ${round(max_change,2)}", file=file)
    print(f"Greatest Decrease: {min_month} ${round(min_change,2)}", file=file)

print("Financial Analysis")
print("------------------------")
print("Total Months: " + str(total_months))
print(f"Total Profit: ${total_profit}")

print(f"Average Change: ${round(average,2)}")

print(f"Greatest Increase: {max_month} ${round(max_change,2)}")
print(f"Greatest Decrease: {min_month} ${round(min_change,2)}")