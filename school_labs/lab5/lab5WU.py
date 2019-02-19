import random

def main():

    total = 10000
    histogram = [0]*11
    i = 1
    while i <= 10000:
        x = random.randint(1,6)
        y = random.randint(1,6)
        sum_amt = x + y
        histogram[sum_amt-2] += 1
        i += 1

    print(histogram)

if __name__ == "__main__":
    main()
