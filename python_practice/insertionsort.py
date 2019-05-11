# def insertion_sort(l):
#     for i in range(1, len(l)):
#         print("List at the beginning of for Loop: {0}".format(l))
#         j = i-1
#         key = l[i]
#         print("key is {0}".format(key))
#         print("Key is smaller than {0}".format(l[j]))
#         while (l[j] > key) and (j >= 0):
#
#            print("The list before sorting: {0}".format(l))
#            print("changing with {0}th index which is {1} with {2}".format(j+1,l[j+1],l[j]))
#            l[j+1] = l[j]
#
#            print(l)
#            print("Round {0}".format(i))
#            print("")
#            j -= 1
#         print("While loop done")
#         l[j+1] = key
#         print("After changing l[j+1] = Key: {0}".format(l))
#         print("")
#
# print(insertion_sort([6,1,2,8,1,4,1,6,4,7]))



def insertionsortWithbin(seq):
    for i in range(1, len(seq)):
        key = seq[i]
        print("key is: {0}".format(key))

        low, up = 0, i
        print("low is: {0} and up is: {1}".format(low,up))
        while up > low:
            print("Up is greater than Low")
            middle = (low + up) // 2
            print("Middle is: {0}".format(middle))
            if seq[middle] < key:
                print("{0} is smaller than Key, {1}".format(seq[middle],key))
                low = middle + 1
                print("new low: {0}".format(low))
            else:
                up = middle
                print("new up: {0}".format(up))
            print("while loop done")
            print("")
            print("New set of Low and Up: ({0},{1})".format(low,up))

        print("seq[:] = seq[:{0}] + [{1}] + seq[{0}:{2}] + seq[{3}:]".format(low,key,i,i+1))
        seq[:] = seq[:low] + [key] + seq[low:i] + seq[i + 1:]
        print(seq)
        print("")
    print(seq)


insertionsortWithbin([6,1,2,8,3])
