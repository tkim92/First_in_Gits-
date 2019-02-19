
def slope(x1,x2,y1,y2):
    y_d = y2 - y1
    x_d = x2 - x1

    if x_d != 0:
        slope = y_d / x_d
        return slope
    else:
        return 0



def main():
    a = float(input(str("Enter first x value: ")))
    c = float(input(str("Enter first y value: ")))
    b = float(input(str("Enter second x value: ")))
    d = float(input(str("Enter second y value: ")))
    m = slope(a,b,c,d)
    if m != 0:
        y_intercept = d - m * b
        print("y = " + str(m)+" x + " + str(y_intercept))
    else:
        print("Slope Not Exist")

if __name__ == "__main__":
    main()
