import csv
def process_data():
    with open("data.csv", "r") as file:
        reader = csv.DictReader(file)

        print("\n EMPLOYEE DETAILS")

        for row in reader:
            print("name: ", row["name"])
            print("roll no: ", row["roll_no"])
            print("department: ", row["department"])
            print("timing of job: ", row["timing_of_job"])


process_data()
        
