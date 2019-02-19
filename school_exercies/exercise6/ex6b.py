def separate(phrase):
    new_phrase = ""
    for i in phrase:
        if i.isupper() == True:
            new_phrase = new_phrase + " " + i
        else:
            new_phrase += i
    new_phrase = new_phrase.lstrip()
    return new_phrase.capitalize()

def combine(phrase):
    new_phrase = ""
    plist = phrase.split()
    for i in plist:
        i = i.capitalize()
        new_phrase += i
    return new_phrase
