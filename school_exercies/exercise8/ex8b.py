def reverseTel(phonebook):
    reverseone = {}

    for i in phonebook:
        if phonebook[i] in reverseone:
            reverseone[phonebook[i]] += i
        else:
            reverseone[phonebook[i]] = i
    return reverseone


x = {'Smith, Jane':'123-4567','Doe, John':'987-6543','Baker,David':'567-8901'}
