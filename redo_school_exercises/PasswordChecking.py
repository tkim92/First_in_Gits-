import numpy as np

# Ex4.B Password Checking

def passwordCheck(password):
    checking = np.array([0,0,0,0])
    condition = np.array([8,1,2,1])
    for i in password:
        checking[0] += 1
        if str(i).isupper() == True:
            checking[1] += 1
        elif i.isdigit():
            checking[2] += 1
        elif i.isdigit() == False and i.isalpha() == False:
            checking[3] += 1

    if len(checking[checking >= condition]) == 4:
        return("{0} is a valid".format(password))
    else:
        return("{0} is not a valid password".format(password))


def main():
    mypassword = input("enter a password: ")
    print(passwordCheck(mypassword))

if __name__ == '__main__':
    main()
