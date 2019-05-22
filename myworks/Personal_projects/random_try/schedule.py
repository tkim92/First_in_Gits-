"""
Remove duplicate schdules.

1. Provide testing number
2. Provide number of classes the user wishes to take
3. Provide schedules of classes
4. Output the maximum number of classes available based on provided schedules


 MON,TUE, WED, THU, FRI : day
 A,B,C,D,E: time

 Each class has two lectures per week

 User provides classes with its schdule manually
  -> THU C FRI D
  -> FRI B TUE E

  ...

 If any duplicates, remove only one of the duplicates.


"""



        #
        #
        # print("Test Case #%d\n%d"%(i,len(by_class)))


def schedule(n):
    flag = "Green"
    subject_list = []
    all_schedule = []

    for i in range(n):
        mysubject = input("Provide subject schedules (etc. MON A,TUE C): ").split(",")

        for i in mysubject:
            if i in subject_list:
                flag = "Red"
                break
            else:
                flag = "Green"

        if flag == "Green":
            subject_list.append(mysubject[0])
            subject_list.append(mysubject[1])
            all_schedule.append(mysubject)

    return len(all_schedule)


def main():

    Trials = int(input("How many tests do you want to run?: "))

    for i in range(1,Trials+1):
        number_of_class = int(input("How many classes do you want to take?: "))
        print(("Test Case #%d\n%d"%(i,schedule(number_of_class))))


if __name__ == "__main__":
    main()
