def response(hey_bob):
    '''
    Determines the response Bob will give to someone

    Args:
        hey_bob (string): what someone said to Bob

    Returns:
        string: Bob's answer
    '''
    answer = ''
    clean_hey_bob = hey_bob.strip() # removing any white spaces from the original string
    
    if not clean_hey_bob:
        answer = 'Fine. Be that way!'
    elif clean_hey_bob[-1] == '?':
        if clean_hey_bob.isupper():
            answer = 'Calm down, I know what I\'m doing!'
        else:
            answer = 'Sure.'
    elif clean_hey_bob.isupper():
        answer = 'Whoa, chill out!'
    else:
        answer = 'Whatever.'

    return answer