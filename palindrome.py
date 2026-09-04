# we are going to check if a word or sentence is a palindrome afetr normalizing case and ignoring unnecessary spaces.

# normalize the input first
# Python supports string slicing 

#consider spaces and capitalization

#objective is to build string manipulation and comparison logic.

#palindrome checker 
#check the valid and invalid output 

#palindrome = input("Enter the palindrome: ")
#check the palindrome is or not 
#is_palindrome = palindrome.reverse() == palindrome
#supports string slicing 
#is_palindrome = palindrome[::-1]
#why is the logic[::-1] used?
## The logic [::-1] is used to reverse the string. In Python, slicing allows you to create a new string by specifying a start, stop, and step. By using -1 as the step, it tells Python to take the string from the end to the beginning, effectively reversing it. This is a concise and efficient way to check if a string is a palindrome by comparing the original string with its reversed version.

#check the input valid or not 
#is_palindrome = palindrome[::-1] == palindrome

palindrome = input("Enter the palindrome: ")
is_palindrome = palindrome.lower().replace(" ", "")[::-1] == palindrome.lower().replace(" ", "")

reversed_text = palindrome[::-1]

if is_palindrome:
    print("THE INPUT IS A PALINDROME")
else:
    print("THE INPUT IS NOT A PALINDROME")