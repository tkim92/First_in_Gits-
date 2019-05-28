def palindrome(mysentence):
    mysentence = list(mysentence)
    while mysentence:
        if mysentence[0] == mysentence[-1]:
            mysentence.pop(0)
            mysentence.pop(-1)
        else:
            return False

    return True
