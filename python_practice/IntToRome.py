def intToRoman(num):
    mylist = [1000,100,10,1]
    thousands = {0:"", 1:"M", 2:"MM", 3:"MMM"}
    hundreds = {0:"", 1:"C", 2:"CC", 3:"CCC", 4:"CD", 5:"D", 6:"DC", 7:"DCC", 8:"DCCC", 9:"CM"}
    tens = {0:"", 1:"X", 2:"XX", 3:"XXX", 4:"XL", 5:"L", 6:"LX", 7:"LXX", 8:"LXXX", 9:"XC"}
    digits = {0:"", 1:"I", 2:"II", 3:"III", 4:"IV", 5:"V", 6:"VI", 7:"VII", 8:"VIII", 9:"IX"}

    myrome = [thousands,hundreds,tens,digits]
    mynumber = [num//i%10 for i in mylist]

    Rome = ""

    for myindex, myint in enumerate(mynumber):
        Rome += myrome[myindex][myint]

    return(Rome)
