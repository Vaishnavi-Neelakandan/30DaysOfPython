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
length = int(input("Enter the password length: "))

# Make sure password is at least 1 character long
if length < 1:
    print("Password length must be at least 1")
else:
    # Step 3: Ensure the first character is a letter
    first_char = random.choice(lowercase_letters + uppercase_letters)

    # Step 4: Generate the remaining characters
    remaining_chars = ""
    for i in range(length - 1):
        remaining_chars += random.choice(input_string)

    # Step 3: Combine and display the password
    password = first_char + remaining_chars
    print("Generated Password:", password)
