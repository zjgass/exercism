def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")

    totalSum = 0

    for x in range(1, number//2+1):
        if number%x == 0:
            totalSum += x

    if totalSum == number:
        return 'perfect'
    elif totalSum > number:
        return 'abundant'
    else:
        return 'deficient'
