def leap_year(year):
    """

    :param year: int - the year to test if it is a leap year
    :return: bool - if the year is a leap year
    """

    return (year % 400 == 0
            or (year % 4 == 0
            and year % 100 != 0))
