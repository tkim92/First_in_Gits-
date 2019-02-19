def reverseNum(n):
    if n < 10:
        print(n)
    else:
        print(n%10,end="")
        reverseNum(n//10)

def maxValue(vals):
    if len(vals) > 1:
        if vals[0] < vals[1]:
            del vals[0]
            maxValue(vals)
        else:
            del vals[1]
            maxValue(vals)
    else:
        return vals[0]
