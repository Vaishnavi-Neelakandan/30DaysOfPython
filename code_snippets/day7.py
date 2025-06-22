#Day 7 Count word frequencies in file

# Step 1: Open the file in read mode

def count_words(filename):
    try:
        with open(filename, "r") as file:
            content = file.read().lower()  # Read the entire content and Convert text to lowercase (to make counting case-insensitive)
    except FileNotFoundError:
        print(f"File does not exist. Please try again with correct filename")
        return filename
    
# Step 2: Remove punctuation
    for char in ",.!?":
        content = content.replace(char, "")

# Step 3: Split the text into words
    words = content.split()

# Step 4: Create an empty dictionary to store word counts
    word_count = {}

# Step 5: Loop through each word
    for word in words:
        if word in word_count:
            word_count[word] += 1  # If word exists, add 1
        else:
            word_count[word] = 1   # If new word, set count to 1

# Step 6: Print the word frequencies
    for word, count in word_count.items():
        print(f"{word}: {count}")

count_words("sample.txt")
