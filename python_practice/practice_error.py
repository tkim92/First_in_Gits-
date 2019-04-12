def testing1(mystring):
    try:
        if mystring.isalpha():
            print("correct")
            return "YESSS"
    except:
        print("Wrong, input the string.")
    return "Do it again"




#
# testing1("ABC")
testing1("123")
#
# Why the testing1("123") only returns "Do it again"?
# It's because, "123" is technically a string. and even though it's not a alphabet,
# it does not occur the error, but instead just having False value.
