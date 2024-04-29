import hypotenuse


def my_sum(a, b):
    """
    Return the sum of the two arguments.

    :param a: the first number
    :param b: the second number
    :return: the sum of the numbers
    """
    return a + b


def my_multipy(a, b):
    """
    Return the multiplication of the two arguments.

    :param a: the first number
    :param b: the second number
    :return: the multiplication of the numbers
    """
    return a * b


def my_divide(a, b):
    """
    Return the division of the two arguments.

    :param a: the first number
    :param b: the second number
    :return: the division of the numbers
    """
    if b != 0:
        return a / b
    else:
        return "0 can't divide the number"


def my_subtract(a, b):
    """
    Return the subtraction of the two arguments.

    :param a: the first number
    :param b: the second number
    :return: the subtraction of the numbers
    """
    return a - b


def calculator():
    """
    A simple calculator that performs addition, subtraction, multiplication, or division based on user inputs.
    """
    a = float(input("enter the first number: "))
    b = float(input("enter the second number: "))
    print("1 to add")
    print("2 to subtract")
    print("3 to multiply")
    print("4 to divide")
    print("5 to calculate hypotenuse")
    choice = int(input())
    if choice == 1:
        result = my_sum(a, b)
        print(result)
    elif choice == 2:
        result = my_subtract(a, b)
        print(result)
    elif choice == 3:
        result = my_multipy(a, b)
        print(result)
    elif choice == 4:
        result = my_divide(a, b)
        print(result)
    elif choice == 5:
        result = hypotenuse.calculate_hypotenuse(a, b)
        print(result)
    else:
        print("Wrong choice")


def main():
    """
    Main function to run the calculator.
    """
    calculator()


if __name__ == "__main__":
    """
    entry point of the main function
    """
    main()
