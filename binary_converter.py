from re import match


def binary_converter():
    # Main function. First takes input from user and assigns it proper action.
    user_input = take_proper_input()

    if user_input[1] == "2":
        decimal_number = binary_to_decimal(user_input[0])
        output(decimal_number, "10")
    else:
        binary_number = decimal_to_binary(int(user_input[0]))
        output(binary_number, "2")


def take_proper_input():
    # Instruction if user gives invalid input.
    invalid_input = ("\nInvalid input.\n"
                     "Proper input format is:\n"
                     "\"number to convert\" + \"space character\""
                     "+ \"actual system (2 or 10)\"\n"
                     "fe. \"4583 10\" or \"1010 2\"\n")

    user_input = input("Your Input: \n")
    # Regular expression allows only binary input (then 2)
    # or decimal input (then 10). It allows to avoid situation
    # when user will type decimal number and declare as binary.
    while not match("^[01]+ 2$|^\d+ 10$", user_input):
        print(invalid_input)
        user_input = input("Your Input: \n")
    # Return 2 elements list where first element is number to convert
    # an second inform is it decimal (10) or binary (2).
    return user_input.split(" ")


def binary_to_decimal(binary_number):
    # Split given number for single digits and reverse them
    # what alows to use simpler for loop.
    binary_number_splited = list(binary_number)
    binary_number_splited.reverse()
    # For loop to convert binary_number to decimal_number
    decimal_number = 0
    index = 0
    for i in binary_number_splited:
        decimal_number += int(i) * (2 ** index)
        index += 1

    return decimal_number


def decimal_to_binary(decimal_number):
    binary_number = []
    # Loop to convert decimal_number to binary_number
    # It appends numbers to list created above
    while True:
        result = int(decimal_number / 2)
        reminder = decimal_number % 2
        # Append as string to allow join list later
        binary_number.append(str(reminder))
        decimal_number = result
        if result == 0:
            break

    binary_number.reverse()
    binary_number = "".join(binary_number)
    return binary_number


def output(number, binary_or_decimal):
    top_and_botom = "-" * (len(str(number)) + len(binary_or_decimal) + 5)
    print("/{}\ ".format(top_and_botom))
    print("| {} | {} |".format(number, binary_or_decimal))
    print("\{}/ ".format(top_and_botom))


binary_converter()
