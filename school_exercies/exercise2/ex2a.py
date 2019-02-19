
def bmr(g,w,h,a):
    if g == 1:
        BMR_male = 66 + (6.3 * w) + (12.9 * h) - (6.8 * a)
        return BMR_male
    else:
        BMR_female = 655 + (4.3 * w) + (4.7 * h) - (4.7 * a)
        return BMR_female


def main():
    G = int(input("Enter your gender (1 for male & 2 for female): "))
    W = float(input("Enter your weight in pounds: "))
    H = float(input("Enter your height in inches: "))
    A = int(input("Enter your age in years: "))

    result = bmr(G,W,H,A)

    print("your BMR is " + str(result) + " and the number of chocolate bars is " + str(result/230))

if __name__ == '__main__':
    main()
