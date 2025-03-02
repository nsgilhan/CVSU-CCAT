# Function to check whether a number is odd or even
def check_odd_even(number):
    if number % 2 == 0:
        return f"{number} is Even"
    else:
        return f"{number} is Odd"

# Get input from the user
num = int(input("Enter a number: "))

# Check and print if the number is odd or even
result = check_odd_even(num)
print(result)
