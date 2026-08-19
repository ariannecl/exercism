def response(hey_bob):
    '''
    Determines the response Bob will give to someone

    Args:
        hey_bob (string): what someone said to Bob

    Returns:
        string: Bob's answer
    '''
    answer = ''
    new_hey_bob = hey_bob.strip() # removing any white spaces from the original string
    
    if new_hey_bob == '':
        answer = 'Fine. Be that way!'
    elif new_hey_bob.isupper() and hey_bob[-1] == '?':
        answer = 'Calm down, I know what I\'m doing!'
    elif new_hey_bob[-1] == '?':
        answer = 'Sure.'
    elif new_hey_bob.isupper():
        answer = 'Whoa, chill out!'
    else:
        answer = 'Whatever.'

    return answer