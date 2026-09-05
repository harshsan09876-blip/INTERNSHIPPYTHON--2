# Day 13 - Prime Number Analyzer

# Take a number from the user
number = int(input("Enter a number: "))


# Create a function to check prime number
def is_prime(number):

    # 0, 1 and negative numbers are not prime
    if number < 2:
        return False

    # Use for loop to check possible divisors
    # Avoid unnecessary checks by using square root
    for i in range(2, int(number**0.5) + 1):

        # If number is exactly divisible, it is not prime
        if number % i == 0:
            return False

    # No divisor found, so number is prime
    return True


# Check the entered number
if is_prime(number):
    print("Prime")
else:
    print("Not Prime")


# Take starting and ending numbers
start_number = int(input("Enter start number: "))
ending_number = int(input("Enter ending number: "))


# Check every number in the given range
for i in range(start_number, ending_number + 1):

    # Reuse the prime checking function
    if is_prime(i):
        print(i, end=" ")