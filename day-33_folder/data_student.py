# build a python based CLI.
# which contains student details, subjects, marks, grades, and academic performance.

# add, update, search, view, and generate records.

# step 1: create the student data structure.
students = [
    {
        "id": "101",
        "name": "HARSH CHAUHAN",
        "marks": {
            "dsa": 89,
            "python": 90,
            "dstl": 89,
        },
    },
    {
        "id": "102",
        "name": "JATIN CHAUDHARY",
        "marks": {
            "dsa": 90,
            "python": 80,
            "dstl": 78,
        },
    },
    {
        "id": "103",
        "name": "MUNENDRA PRATAP SINGH TARKAR",
        "marks": {
            "dsa": 67,
            "python": 78,
            "dstl": 99,
        },
    },
    {
        "id": "104",
        "name": "SANDEEP BAGHEL",
        "marks": {
            "dsa": 88,
            "python": 90,
            "dstl": 90,
        },
    },
    {
        "id": "105",
        "name": "PRABAL SHARMA",
        "marks": {
            "dsa": 78,
            "python": 89,
            "dstl": 99,
        },
    },
]


#step 2 : build the cli

def add_students():
    pass

def update_students():
    pass

def search_students():
    pass

    #step 3:  cli data ko display karna hai.
        
def view_students():
    for student in students:
        print("ID: ", student["id"])
        print("name: ", student["name"])
        print("marks: ", student["marks"])
        print("------------")
        
        
        
    pass

def performance_summary():
    pass



while True:
    
    print("\n STUDENT RESULT MANAGEMENT||||")
    print("\n1.ADD RESULT")
    print("\n2. update result")
    print("\n3. search result")
    print("\n4. view result")
    print("\n5.performance summary of student")
    print("\n6. Exit")
    
    
    choice = input("ENTER THE CHOICE: ")
    
    if choice == "1":
        add_students()
        
    elif choice == "2":
        update_students()
        
    elif choice == "3":
        search_students()
        
    elif choice == "4":
        view_students()
        
    elif choice == "5":
        performance_summary()
        
    elif choice == "6":
        print("Program closed")
        break
    
    else:
        print("Invalid choice")
        
        
    
    
    
    
    