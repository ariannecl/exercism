def leap_year(year):
    '''
    Determines if a year is a leap year

    Args:
        year (int): year to be checked

    Returns:
        bool: True if it is a leap year, False otherwhise
    '''
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 != 0:
            return False
        return True
    return False