#Day 4 Check is the user entered number is prime or not

def is_prime(num):
    if num < 2:
        print(f"{num} is neither prime nor composite") 
        return

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print(f"{num} is not a prime number")
            return

    # If loop completes with no factors, it's prime
    print(f"{num} is a prime number")

# User input
num = int(input("Enter a number to check: "))
is_prime(num)