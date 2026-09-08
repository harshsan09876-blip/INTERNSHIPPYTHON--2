import csv
import os

print("Python is running")
print("Current folder:")
print(os.getcwd())

print("\nFiles in this folder:")
print(os.listdir())
print("Program started")

try:
    with open("data.csv", "r") as file:
        reader = csv.DictReader(file)

        print("CSV opened successfully")
        print("Headers:", reader.fieldnames)

        for row in reader:
            print("Name:", row["Name"])
            print("Roll No:", row["Roll_No"])
            print("Department:", row["Department"])
            print("Timing:", row["Timing"])

except Exception as e:
    print("ERROR:", e)