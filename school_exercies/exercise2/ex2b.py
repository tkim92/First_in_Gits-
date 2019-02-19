
def windchill():
    t = float(input(str("Enter temperature (F): ")))
    v = float(input(str("Enter wind velocity(MPH): ")))

    t_wc = 35.74 + 0.6215*t - 35.75*v**0.16 + 0.4275*t*v**0.16

    print(str("The windchill is ") + str(t_wc))

def main():
    windchill()

if __name__ == '__main__':
    main()


# How to continue to stay in the function? As in... after resulting the output, how to continue
# to have "Enter temperature (F): "
