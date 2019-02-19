

def dna(adna):
    # raw_DNA = input("Enter a DNA sequence: ")
    rg = adna
    glist = []
    scolon = ["TAG","TAA","TGA"]

    i = 0
    while i < len(rg):
        if i == rg.find("ATG"):
            rg = rg[i+3:]

            sindex = []
            for stop_index in scolon:
                index = rg.find(stop_index)
                # if find fails to find what i want, it returns -1
                # usually 0 is the default failure return value, unless 0 can be a possible answer
                if index != -1:
                    sindex.append(index)
            smallest = min(sindex)
            glist.append(rg[:smallest])
            rg = rg[smallest + 3:]

            i = 0
        else:
            i += 1
    return glist

def main():
    raw_DNA = input("Enter a DNA sequence: ")
    final_list = dna(raw_DNA)
    i = 0
    while i < len(final_list):
        print("gene {0} {1}".format(i,final_list[i]))
        i += 1

if __name__ == "__main__":
    main()
