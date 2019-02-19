def compound_interest(S,T,I):
    interest = 1 + I
    count = 0
    total = S
    while total < T:
        total *= interest
        count += 1
    return count

def main():
    a = float(input("Enter starting amount: "))
    b = float(input("Enter target amount: "))
    c = float(input("Enter interest rate: "))

    print(str(compound_interest(a,b,c)) + " years")

if __name__ == "__main__":
    main()
