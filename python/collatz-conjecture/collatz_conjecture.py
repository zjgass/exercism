def steps(number):
    """

    :param number: int - the initial number for which to count steps in the
    Collatz Conjecture.
    :return: int - how many steps were required to get to 1.
    """

    if number < 1:
        raise ValueError("Only positive integers are allowed")
    elif number == 1:
        return 0
    elif number % 2 == 0:
        number = number / 2
    else:
        number = 3 * number + 1

    return 1 + steps(number)
