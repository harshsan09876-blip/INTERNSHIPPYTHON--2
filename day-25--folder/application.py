#making a file which is based on the formatting , data handling.
# roadmap of file processing:
#     1) define a funcvtion for Name
#     2) then made a  name as dictionary
#     3) function
#     4) email sample
#     5) function
#     6) company Name
#     7) function
#     8) position
#     9) execute it.
    #    10) then made the people name in new file as people.py
    
from people import people

def employee_name(people):
    formatted = []
    n = len(people)
    for i in range(0, n):
        num = people[i]
        formatted_name = num["name"].title()
        formatted.append(formatted_name)

    return formatted


formatting = employee_name(people)
print(formatting)


        
        