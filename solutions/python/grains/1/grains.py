def square(number):
    if number > 64 or number < 1:
        raise ValueError("square must be between 1 and 64")
    
    grains = 1
    if number > 1:
        grains = 2 ** (number - 1)
    return grains


def total():
    n = 63
    total = 1
    while n > 0:
        total += 2 ** n
        n -= 1

    return total
