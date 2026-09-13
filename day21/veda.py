import json
import os

# Get the folder where python.py is located
folder = os.path.dirname(os.path.abspath(__file__))

# Create the complete path of data.json
file_path = os.path.join(folder, "data.json")

# Open and read JSON file
with open(file_path, "r") as file:
    candidate = json.load(file)

# Search candidate
search = input("Enter the candidate name: ")

found = False

for i in candidate:
    if i["name"].lower() == search.lower():
        print("\nCandidate Found!")
        print("Name:", i["name"])
        print("Class:", i["class"])
        print("Roll No:", i["rollno"])
        print("Subject:", i["subject"])
        print("CGPA Status:", i["cgpa_status"])

        found = True
        break

if not found:
    print("\nCandidate not found.")