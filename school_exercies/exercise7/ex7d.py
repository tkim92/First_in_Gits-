def spaceit(istr):
    if len(istr) == 1:
        return istr[0]
    else:
        if istr[0] == istr[1]:
            return istr[0] + " " + spaceit(istr[1:])
        return istr[0] + spaceit(istr[1:])

def main():
    astr = input("Enter your string: ")

    print(spaceit(astr))

if __name__ == "__main__":
    main()
