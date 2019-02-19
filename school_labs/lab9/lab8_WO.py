def rankandSuitCount(cards):
    r = {}
    s = {}
    for i in cards:
        if i[0] in r:
            r[i[0]] += 1
        else:
            r[i[0]] = 1

        if i[1] in s:
            s[i[1]] += 1
        else:
            s[i[1]] = 1
    return (r,s)

alist = [ 'AS', 'AD', '2C', 'TH', 'TS' ]

rank,suit = rankandSuitCount(alist)


def isSequence(alist):

    mylist = []
    strdic = {'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'T':10,'J':11,'Q':12,'K':13,'A':14}
    #
    # print(alist)
    for i in alist:
        #
        # print(i)
        mylist.append(strdic[i])

    mylist.sort()

    for j in mylist[:-1]:
        if j + 1 not in mylist:
            return False
    return True

    # do the subtraction = -5

def pokerHand(cards):
    rank,suit = rankandSuitCount(cards)

    r_val = list(rank.values())
    s_val = list(suit.values())

    r_key = list(rank.keys())
    s_key = list(suit.keys())


    if len(rank) == 5:
        if isSequence(r_key) == True and len(suit) == 1:
            return("Straight-Flush!")
        elif isSequence(r_key) == False and len(suit) == 1:
            return("Flush!")
        elif isSequence(r_key) == True and len(suit) != 1:
            return("Straight!")
        else:
            return("High-card")
    elif len(rank) == 4:
        return("One Pair")
    elif len(rank) == 3:
        if 3 in r_val:
            return("Three-of-a-Kind")
        else:
            return("Two Pairs")
    elif len(rank) == 2:
        if 4 in r_val:
            return("Four-of-a-Kind")
        else:
            return("Full-House")


x1 = ['8D','9D','TD','JD','QD']
x2 = ['5C','5S','5D','5H','9C']
x3 = ['6H','6S','6C','QD','QH']
x4 = ['3H','6H','TH','JH','AH']
x5 = ['2S','3D','4H','5H','6S']
x6 = ['2C','2H','2D','7S','3D']
x7 = ['AH','AD','QS','QH','2C']
x8 = ['8S','8C','9D','3S','TH']
x9 = ['4H','7D','KS','AS','9C']

print(pokerHand(x1))
print(pokerHand(x2))
print(pokerHand(x3))
print(pokerHand(x4))
print(pokerHand(x5))
print(pokerHand(x6))
print(pokerHand(x7))
print(pokerHand(x8))
print(pokerHand(x9))
