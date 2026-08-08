def steps(number):
    '''
    Calculate how many steps it takes so a number reaches 1 using Collatz Conjecture

    Args:
        number: int.

    Returns:
        int indicating how many steps it took to reach 1.

    Raises:
        ValueError: If number is less than or equal to zero.
    '''
    if number <= 0:
        raise ValueError('Only positive integers are allowed')
    
    counter = 0
    while number > 1:
        if number % 2 == 0:
            number /= 2
        else:
            number = (number * 3) + 1
        counter += 1

    return counter