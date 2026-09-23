# build a password generator.

# first of all start with functions.
# then values assign for those numbers in multiple test case.
# split the number and assert the number in two segments.
# generate the password by using random module.

import string
import secrets

try:
    upper_case = input("Uppercase characters? (Y OR M): ").upper()
    lower_case = input("Lowercase characters? (Y OR M): ").upper()
    digits = input("Digits? (Y OR M): ").upper()
    special_characters = input("Special characters? (Y OR M): ").upper()

    NARUTO = ""
    if upper_case == "Y":
        NARUTO += string.ascii_uppercase

    GOJO = ""
    if lower_case == "Y":
        GOJO += string.ascii_lowercase

    KASHIMO = ""
    if digits == "Y":
        KASHIMO += string.digits

    SAKURA = ""
    if special_characters == "Y":
        SAKURA += string.punctuation

    character_pool = ""
    character_pool += NARUTO
    character_pool += GOJO
    character_pool += KASHIMO
    character_pool += SAKURA

    password_length = int(input("THE LENGTH OF PASSWORD: "))

    if not character_pool:
        raise ValueError("At least one character type must be selected.")

    if password_length <= 0:
        raise ValueError("Password length must be greater than 0.")

    password = ""

    for i in range(password_length):
        character = secrets.choice(character_pool)
        password += character

    print("Generated Password:", password)

except ValueError as e:
    print("Error:", e)

except Exception as e:
    print("Unexpected Error:", e)