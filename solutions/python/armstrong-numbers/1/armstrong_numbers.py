def is_armstrong_number(number):
    """
    Defines if a number is an Armstrong number

    Args:
        number (int): The number to be checked.

    Returns:
        bool: wether the number is an Armstrong number or not
    """
    number_string = str(number)
    digits = len(number_string)
    sum = 0

    for i in number_string:
        sum += int(i) ** digits

    return sum == number