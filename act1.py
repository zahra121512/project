def swap_numbers(num1, num2, num3):
    """Swaps two numbers and returns the swapped values.

    Args:
        num1 (int or float): The first number to swap.
        num2 (int or float): The second number to swap.

    Returns:
        tuple: A tuple containing the swapped values (num2, num1).
    """

    return num2, num1, num3 

def main():
    """Main function to get user input and swap the numbers."""

    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    num3 = int(input("Enter the third number: "))

    swapped_numbers = swap_numbers(num1, num2, num3)

    print("Swapped numbers:", swapped_numbers)

if __name__ == "__main__":
    main()