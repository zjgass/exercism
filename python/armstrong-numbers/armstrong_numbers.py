def is_armstrong_number(number):
    """

    :param number: int - the number to check if it is armstrong.
    :return: bool - true if the number is armstrong, false if not.
    """

    isArmstrong = False
    totalSum = 0
    strNum = str(number)
    numberOfDigits = len(strNum)
    for x in range(0,numberOfDigits):
        totalSum += int(strNum[x]) ** numberOfDigits

    if totalSum == number:
        isArmstrong = True

    return isArmstrong
