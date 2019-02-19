def MC(aword):
    aword = aword.upper()
    d = {" ":' ','A':'._','B':'_...','C':'_._.','D':'_..','E':'.','F':'.._.','G':'__.','H':'....','I':'..','J':'.___','K':'_._','L':'._..','M':'__','N':'_.','O':'___','P':'.__.','Q':'__._','R':'._.','S':'...','T':'_','U':'.._','V':'..._','W':'.__','X':'_.._','Y':'_.__','Z':'__..'}

    for i in aword[:-1]:
        if i == '.':
            print(" ")
        else:
            print(d[i])
    print(d[aword[-1]])

def main():
    word = input("Enter a phrase: ")
    MC(word)

if __name__ == '__main__':
    main()
