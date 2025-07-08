# generate_csv.py
import os
import csv

# Create folder if not exists
folder_name = "output"
os.makedirs(folder_name, exist_ok=True)

# Create a CSV file
file_path = os.path.join(folder_name, "data.csv")

with open(file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["ID", "Name", "Score"])
    writer.writerow([1, "Alice", 95])
    writer.writerow([2, "Bob", 88])

print(f"CSV file created at: {file_path}")
