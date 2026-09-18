# mein ek date, time utility workspace banana chatu hoon.
# toh ek dictionary ka data date(**)
# ek time uske corresponding hai 
# working days kitne hai

# date = {
#     "string_1": "16 september 2026",
#     "string_2": "18 september 2026",
#     "string_3": "19 september 2026",
#     "String_4": "20 september 2026",
# }

# time = {
#     "string_5": "2:30 PM",
#     "string_6": "4:30 PM",
#     "string_7": "5:30 PM", 
#     "string_8": "6:30 PM"
# }

# employee_shift = {
#     "string_9": "SAM",
#     "string_10": "BEN",
#     "string_11": "ASHIN",
#     "string_12": "SRAM"
# }


from datetime import datetime

#to calculate the age of person

dob = (input("ENTER THE DOB IN(DD-MM-YYYY): "))


try:
    date_of_birth = datetime.strptime(dob, "%d-%m-%Y")
    current_date = datetime.now()

    age = current_date.year - date_of_birth.year

    if (current_date.month, current_date.day) < (date_of_birth.month, date_of_birth.day):
        age -= 1

    print("DATE OF BIRTH: ", date_of_birth.strftime("%d-%m-%Y"))
    print("CURRENT DATE: ", current_date.strftime("%d-%m-%Y"))
    print("Your age: ", age, "years")

except ValueError:
    print("invalid date format!!")
    print("the time format is revise now")
        
    
    
    