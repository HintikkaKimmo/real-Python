def factor(user_input):
    """factor provides all divisors of user input
    :type user_input: int
    """
    user_input = int(user_input)
    for n in range(1, user_input):
        if user_input % n == 0:
            print("{} a divisor of {}".format(n, user_input))
        n += 1

divider = input("Please provide a number to find divisors: ")
factor(divider)

