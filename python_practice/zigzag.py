
def mine_convert(s,numRows):
        if numRows == 1:
            return s
        else:
            keynum = 2 * numRows - 2
            mystrings = [""] * numRows
            myanswer = ""
            rows = 1

            while rows <= numRows:
                for each_index, each_value in enumerate(s):
                    if each_index % keynum == rows - 1 or each_index % keynum == keynum - rows + 1:
                        mystrings[rows-1] += each_value
                rows += 1

            for eachrow in mystrings:
                myanswer += eachrow
            return myanswer

"""
My answer above stil returns correct answer.
However, I am still disqualified because of "Time Limit Exceeded"

Below is the solution to that.

Things to note:

1. I could've used comprehensive list (line 7)
2. Without having double loops (while loop and for loop), I could've define the row more effectively. Refer the codes Below.
3. Both answers approached this quesiton using "%", but different algorithm.
    -  I set two conditions, but the ideal_answer has important algorithm for numbers between the main columns.
    -  refer to line 46.
4. str.join method -- refer to list methods.
"""


def answer_convert(s, numRows):
    if numRows <= 1:
        return s
    rows = ['' for i in range(0, numRows)]
    for i, c in enumerate(s):
        new_row = i % (2 * numRows - 2)
        # print(new_row,numRows-1)
        if new_row > numRows - 1:
            new_row = 2 * numRows - new_row - 2
        rows[new_row] += c
    return ''.join(rows)


print(bool(mine_convert("LeetCode_problem_number6",3) == answer_convert("LeetCode_problem_number6",3)))
