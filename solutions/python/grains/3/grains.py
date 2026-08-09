def square(number):
    '''
    Defines how many grains are in a specific square

    Args:
        number (int): number of a given square

    Returns:
        int: quantity of grains on given square

    Raises:
        ValueError: if number is less than 1 or more than 64
    '''
    if number > 64 or number < 1:
        raise ValueError("square must be between 1 and 64")
    
    grains = 1
    if number > 1:
        grains = 2 ** (number - 1)
    return grains


def total():
    '''
    Defines total number of grains on the chessboard

    Returns:
        int: quantity of grains on the board
    '''
    squares = 64
    grains = 0
    while squares > 0:
        grains += 2 ** (squares - 1)
        squares -= 1

    return grains
