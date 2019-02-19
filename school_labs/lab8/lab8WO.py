def choose(n,k):
    if k == 0 or k == n:
        return 1
    return choose(n-1,k-1) + choose(n-1,k)

print("5 card poker hands from 52 card deck: {0}".format(choose(52,5)))
print("2 card blackjack hands from three 52 card decks: {0}".format(52*3,2))
