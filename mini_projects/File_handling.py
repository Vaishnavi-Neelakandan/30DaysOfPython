#Day 7 Count word frequencies in file

#Writing contents to file
def write_file(file_name):
    content = input(f"Enter the text to write in the file:\n")
    try:
        with open(file_name,"w") as file:
            file.write(content)
            print(f"\nFile has been created and content has been added.")
    except Exception as e:
        print(f"Error creating file and writing to file: {e}")
        return

#Appending contents to already created file
def append_file(file_name):
    content = input(f"Enter the lines you want to add in the file:\n")
    try:
        with open(file_name,"a") as file:
            file.write("\n" + content)
            print(f"\nLines has been added successfully.")
    except Exception as e:
        print(f"Error appending to file: {e}")
        return

#Reading file contents    
def read_file(file_name):
    try:
        with open(file_name,"r") as file:
            print(file.read())
    except FileNotFoundError:
        print(f"Error reading file or File not found")
        return

#Counting word frequencies from the file
def count_words(filename):
    try:
        with open(filename, "r") as file:
            content = file.read().lower()  # Read the entire content and Convert text to lowercase (to make counting case-insensitive)
    except FileNotFoundError:
        print(f"File does not exist. Please try again with correct filename")
        return filename

    for char in ",.!?":   #Replacing all the punctuation marks with space 
        content = content.replace(char, "")

    words = content.split()
    word_count = {}

    for word in words:
        if word in word_count:
            word_count[word] += 1  # If word exists, add 1
        else:
            word_count[word] = 1   # If new word, set count to 1
    print("\n--- Word Frequencies ---")
    for word, count in word_count.items():
        print(f"{word}: {count}")
    print("-------------------------\n")

#Getting input from user for file handling
def show_menu():
    file_name = "sample.txt"  # Default file name
    while True:
        print("Choose an option:")
        print("1. Write to file")
        print("2. Append to file")
        print("3. Read file")
        print("4. Count word frequencies")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            write_file(file_name)
        elif choice == '2':
            append_file(file_name)
        elif choice == '3':
            read_file(file_name)
        elif choice == '4':
            count_words(file_name)
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.\n")

# Start the menu
show_menu()