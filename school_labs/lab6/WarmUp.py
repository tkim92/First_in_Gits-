def matrix(n,init):
    mymatrix = []
    myrow = []
    for i in range(0,n):
        for j in range(0,n):
            myrow.append(init)
        mymatrix.append(myrow)
        myrow = []
    return mymatrix

def order(m):
    return len(m)

def main():
    num = int(input("Enter your number: "))
    val = int(input("Enter your value: "))

    print(matrix(num,val))
    print(order(matrix(num,val)))

if __name__ == "__main__":
    main()

# def matrix(n,init):
#     alist = []
#     blist = []
#     i = 0
#     j = 0
#     for i in range (0,n):
#         alist.append(blist)
#         # print("first i list {0}".format(alist))
#         for j in range (0,i):
#             blist.append(init)
#             blist[j]
#             # print("first j list {0}".format(alist))
#     return alist
#
# def main():
#     n = int(input("Enter the number of matrix :   "))
#     init = int(input("Enter the number:   "))
#     matrix(n,init)
#     print (matrix(n,init))
#
#
# if __name__ == '__main__':
#     main()
