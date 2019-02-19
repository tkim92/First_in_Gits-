mybook = open('abook','r')
whole_Text = mybook.read()
freqs = {}
for i in whole_Text:
    i = i.lower()
    if i.isalpha() == True:
        if i in freqs:
            freqs[i] += 1
        else:
            freqs[i] = 1
sortfreq = list(freqs.keys())
sortfreq.sort()

finallist = []
for i in sortfreq:
    finallist.append(i + " : " + str(freqs[i]))
print(finallist)
