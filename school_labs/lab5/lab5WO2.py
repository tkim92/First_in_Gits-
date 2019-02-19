
def score(n):

    cards = list(n)

    possible_cards = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']


    sum_amt = 0
    i = 0
    while i < len(cards):
        if cards[i].isdigit() == True:
            sum_amt += int(cards[i])
        elif cards[i] == 'T':
            sum_amt += 10
        elif cards[i] == 'J':
            sum_amt += 10
        elif cards[i] == 'Q':
            sum_amt += 10
        elif cards[i] == 'K':
            sum_amt += 10
        else:
            if sum_amt > 21 or sum_amt + 11 > 21:
                sum_amt += 1
            else:
                sum_amt += 11
        i += 1

    return sum_amt

        # else:
        #     return("Invalid Cards")


def main():

    your_string = str(input("Enter your hand of cards(2-9,T,J,Q,K,A): "))

    print(score(your_string))

if __name__ == '__main__':
    main()
