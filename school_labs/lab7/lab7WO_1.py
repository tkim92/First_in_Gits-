def mysplit(oldstring,delimiter):
    slist = []
    i = 0
    while i < len(oldstring):
        if i == oldstring.find(delimiter):
            slist.append(oldstring[:i])
            oldstring = oldstring[i+1:]
            # why i = 0? you just created a 'new' list.
            # so you want to start from beginning, i.e. at index 0
            i = 0
        else:
            # this will not allow the infinite loop
            i += 1

    slist.append(oldstring)
    return slist
