"""
Leetcode No 20.
Difficulty: EASY


Given a string containing just the characters '(', ')', '{', '}', '[' and ']'
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

"""

# The idea is....
# 1. Inner recursive
# 2. stack - appending/popping

def isValid(s):
        mydict = {")":"(",
             "]":"[",
             "}":"{",
             }

        checking = []

        for i in s:
            # if i is closed bracket, check if there is any open bracket that matches to it.
            if i in mydict:
                # make sure the stack (list) is not empty
                if len(checking) != 0:
                    last_element = checking.pop()
                # if stack is empty, put any arbitrary element
                else:
                    last_element = "a"

                if last_element != mydict[i]:
                    return False
            else:
                checking.append(i)

        if len(checking) == 0:
            return True
        else:
            return False
