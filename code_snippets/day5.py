#Day 5 Calculate sum and avaerage of numbers
user_input = input("Enter the numbers separated by space:")

# Convert input to a list of float numbers
numbers = list(map(float, user_input.split()))  

def num_type(num):
      #Handling both int and float numbers as input and printing accordingly
      return int(num) if num == int(num) else round(num,2)

formatted_numbers = [] # Create an empty list to store formatted numbers
for n in numbers: 
    formatted_numbers.append(num_type(n))
print("You entered:",formatted_numbers) # formatted list
       
#Calculating the sum and average:
def calculate(numbers):
    if numbers:  
        total = sum(numbers)
        average = total / len(numbers)
        print(f"Sum: {num_type(total)} \nAverage: {num_type(average)}")
        return total,average
    else:
        print(f"No results to be displayed")
        return 0,0
# Call the function   
calculate(numbers)