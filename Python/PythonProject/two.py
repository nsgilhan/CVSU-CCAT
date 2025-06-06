def compare_numbers():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if num1 > num2:
            print("The first number is greater than the second number.")
        elif num1 < num2:
            print("The first number is less than the second number.")
        else:
            print("Both numbers are equal.")
    except ValueError:
        print("Invalid input. Please enter numerical values.")


if __name__ == "__main__":
    compare_numbers()
