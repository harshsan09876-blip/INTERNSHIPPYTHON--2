import json

#the files are here for connect the business workflow.
#day - 36

data = [
    {
        "name": "HARSH CHAUHAN",
        "semester": "3rd",
        "marks": 8.09
    },
    {
        "name": "AYUSH VARSHNEY",
        "semester": "3rd",
        "marks": 9.41
    },
    {
        "name" : "JATIN",
        "semester": "3rd",
        "marks": 9.41
    },
    {
        "name" : "HARSHIT",
        "semester": "3rd",
        "marks": 9.09
    },
    {
        "name": "AZAL",
        "semester": "3rd",
        "marks": 9.01
    }
]

name = input("Enter student name: ")

for i in data:
    if i["name"] == name:
        print(i["name"])
        print(i["semester"])
        print(i["marks"])
    
    
#     services = [
#     {
#         "name": "...",
#         "category": "...",
#         "status": "..."
#     },
#     ...
# ]


services = [
    {"name": "AI Development", "category": "AI/ML", "status": "Active"},
    {"name": "Web Development", "category": "Web", "status": "Active"},
    {"name": "Cloud Services", "category": "Cloud", "status": "Active"},
    {"name": "Python Training", "category": "Training", "status": "Active"}
]


name = input("Enter service name: ")

for i in services:
    if i["name"] == name:
        print(i["name"])
        print(i["category"])
        print(i["status"])


# Add new service

service_name = input("ENTER THE NEW SERVICE: ")
category = input("ENTER THE NEW CATEGORY: ")
status = input("ENTER THE NEW STATUS: ")

new_service = {
    "name": service_name,
    "category": category,
    "status": status
}

services.append(new_service)

print("\nNew service added successfully!")


# Save services in JSON file

import json

with open("services.json", "w") as file:
    json.dump(services, file, indent=4)

print("Services data saved successfully.")

#day - 37

programs = [
    
    {
        "name" : "WEB DEVELOPMENT",
        "category" : "TRAINING",
        "status" : "ACTIVE"
    },
    {"name" : "PYTHON PROGRAMMING",
     "category" : "TRAINING",
     "status" : "ACTIVE"
     },
    {"name" : "CLOUD SERVICES",
     "category" : "TRAINING",
     "status" : "ACTIVE"
     },
    {"name" : "AIML PROGRAM",
     "category" : "TRAINING",
     "status" : "ACTIVE"
     }
]

program_name = input("ENTER THE PROGRAM NAME: ")

for i in programs: 
    if i["name"]  == program_name:
        print(i["name"])
        print(i["category"])
        print(i["status"])
        
        
new_program = [
    {
        "name" : "CYBER SECURITY WORKSHOP",
        "category": "TRAINING",
        "status" : "ACTIVE"
    },
    {
        "name" : "DEVOPS PROGRAM",
        "category" : "TRAINING", 
        "status" : "ACTIVE"
    },
    {
        "name" : "GENERATIVE AI WORKSHOP",
        "category" : "TRAINING",
        "status" : "ACTIVE"
    }
]

programs.extend(new_program)

with open("programs.json", "w") as file:
    json.dump(programs, file, indent=4)
    
    
    print("PROGRAM SAVED SUCESSFULLY")