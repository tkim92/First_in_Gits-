# # n,m = map(int,input().split())
# def factorial(n):
#     mul = 1
#     for i in range(1,n+1):
#         mul *= i
#     return mul
# def combination(n,k):
#     # fact = factorial(k)
#     # mul = n-k
#     # for i in range(1,n-k):
#     #     mul *= mul-i
#     # return fact * mul
#     nu = factorial(n)
#     de = factorial(n-k) * factorial(k)
#     return nu/de
# # fact = factorial(n)
# # combination = combination(n,m)*combination(n,m),(factorial(m)*factorial(n-m))
# # print(fact/combination)
# #
# print(combination(100,6))


def factorial(n):
    mul = 1
    for i in range(1,n+1):
        mul *= i
    return mul
def combination(n,k):
    return factorial(n) / (factorial((n-k)) * factorial(k))


print(combination(100,6))
