import random

def ssort(somelist):
    print(somelist)
    i = 0
    while i < len(somelist):
        j = i + 1
        min_index = i
        while j < len(somelist):
            if somelist[min_index] > somelist[j]:
                min_index = j
            j += 1
        somelist[i],somelist[min_index] = somelist[min_index],somelist[i]
        i += 1
    print(somelist)

def main():
    consiting_n = int(input("Enter your integer value: "))

    yourlist = [0]*consiting_n
    index = 0
    while index < consiting_n:
        random_num = random.randint(1,9)
        yourlist[index] += random_num
        index += 1

    random.shuffle(yourlist)

    ssort(yourlist)

if __name__ == '__main__':
    main()
