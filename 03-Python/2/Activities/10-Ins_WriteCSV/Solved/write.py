# Dependencies
import os
import csv

# Specify the file to write to
output_path = os.path.join("..", "output", "new.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
    csvwriter.writerow(['First Name', 'Last Name', 'SSN'])

    # Write the second row
    csvwriter.writerow(['Caleb', 'Frost', '505-80-2901'])



total = 564

output_path = os.path.join("..", "output", "new.txt")

with open(output_path, "w") as txt_file:

    txt_file.write("Summary:\n")
    txt_file.write("------------------------------\n")
    txt_file.write(f"Grand Total: {total}\n")


