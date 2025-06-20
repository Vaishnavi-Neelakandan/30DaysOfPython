# Day 6 - Generate a random 8-character password
import random
import string

# Step 1: Define the character set (uppercase + lowercase letters)
lowercase_letters = string.ascii_lowercase  # a-z
uppercase_letters = string.ascii_uppercase  # A-Z
numbers = string.digits  #numbers
special_char = "@$%^&*!~?"  # I defined only specific special characters instead of all combination used in string.punctuation

# Combine them into one string
input_string = lowercase_letters + uppercase_letters + numbers + special_char
# Step 2: Ask the user how long the password should be
while True:
    length = int(input("Enter the password length: "))
    # Make sure password is at least 1 character long
    if length != 8:
        print("Password length must be 8 characters. Please try again")
    else:
    # Step 3: Ensure the first character is a letter
        password = ""
        for i in range(length):
            random_char = random.choice(input_string)
            password += random_char
        print("Generated Password:", password)
        break 
