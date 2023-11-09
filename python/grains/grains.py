def square(number):
    """

    :param number: int - which square.
    :return: int - how many grains are on a given square.
    """

    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")

    return 2 ** (number - 1)


def total():
    """

    :return: int - the total of grains on all squares of the chess board.
    """

    totalSum = 0
    for i in range(1, 65):
        totalSum += square(i)

    return totalSum
