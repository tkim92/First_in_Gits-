def main():

    word_list = []
    your_word = (input("Enter your world: "))

    while your_word != "":

        i = 1
        stop = False
        while i < len(your_word) and stop == False:
            if your_word[0].lower() == your_word[i].lower():
                word_list.append(your_word)
                stop = True
            i += 1

        your_word = (input("Enter your world: "))

    print(word_list)

if __name__ == '__main__':
    main()
