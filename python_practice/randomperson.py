import random

# Use function below to generate number representing a random person among N
def random_person(N, me, source):
    """Generates a uniform random integer between 0 and N-1 but
     excluding the values of me and source.

     Arguments:
       N      Range; must be strictly greater than 1 if source == me,
                and strictly greater than 2 if source != me,
                otherwise behavior is undefined
       me     First value to exclude; must be between 0 and N-1
       source Second value to exclude; must be between 0 and N-1,
                and may be the same as the first.

      Returns:
        Uniform random integer between 0 and N-1 excluding me and src."""


    """
    'Me' is not included in propagating rumors since it circles within the guests only
    """

    M = N-1 if me == source else N-2
    i = min(me, source)
    j = max(me, source)
    p = random.randrange(M)
    if p >= i:
        p += 1
    if p >= j and source != me:
        p += 1
    return p
#
#
def rumors(N,T):


    all_expected_values = []
    how_many_all_knew = 0


    for i in range(T):
        all_expected_values.append(random_person(N,0,1))

    for j in all_expected_values:
        if j == N-2:
            how_many_all_knew += 1

    #
    # print("Expected values")
    # print((1/(N-1))*((1/(N-2))**(N-1)))
    # print((1/2)*(1 + N))

#
#
#     return(how_many_all_knew / T,(1/2)*(min(all_expected_values)+max(all_expected_values)))
#
#
# print(rumors(5,100))




print(rumors(5,50))

#
#
#
#
#     probability = (1/(N-1))*((1/(N-2))^(N-1))
#     expected_value = (1/2)(1 + N)
#
#
