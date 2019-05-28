# Fibonacci Sequence

def fiboSeq(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    return (fiboSeq(n-2) + fiboSeq(n-1))
