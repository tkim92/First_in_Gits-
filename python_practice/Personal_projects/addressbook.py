import os
import csv

def phonebook(menu):
    if menu == 0:
        return False

# Adding New address when menu = 1
    elif menu == 1:

        newName = input("Enter New Name: ")
        newNum = int(input("Enter New Phone Number: "))
        newAge = int(input("Enter New Age: "))
        newAddress = input("Enter New Address: ")
        new_info = [newName,newNum,newAge,newAddress]

        mybook = open("addressbook.csv","a",newline = "")
        adding = csv.writer(mybook)
        adding.writerow(new_info)
        print("Adding Completed!")

        mybook.close()

# Searching information when menu = 2
    elif menu == 2:

        mydict = {"Name":"Enter the name: ",
                "Phone":"Enter the number: ",
                "Age":"Enter the age: ",
                "Address":"Enter the address: "}


        mybook = open("addressbook.csv","r",newline = "")
        searching = csv.reader(mybook)
        asList = list(searching)
        header = asList[0]

        category = input("Select searching method (Name/Phone/Age/Address): ")
        details = input(mydict[category])
        myindex = header.index(category)

        for each_info in asList:
            if str(each_info[myindex]) == details:
                print(each_info)

        mybook.close()





# Deleting the selected information when menu = 3
    elif menu == 3:
        mydict = {"Name":"Enter the name that you want to delete : ",
                "Phone":"Enter the number that you want to delete : ",
                "Age":"Enter the age that you want to delete : ",
                "Address":"Enter the address that you want to delete : "}


        mybook = open("addressbook.csv","r",newline = "")
        searching = csv.reader(mybook)
        asList = list(searching)
        header = asList[0]

        category = input("Select searching method (Name/Phone/Age/Address): ")
        details = input(mydict[category])
        myindex = header.index(category)

        deleting_list = []

        for each_info in asList:
            if str(each_info[myindex]) == details:
                deleting_list.append(each_info)
        # deleting_list = [each_info if str(each_info[myindex]) == details for each_info in asList]

        if len(deleting_list) == 0:
            print("No information found")

        elif len(deleting_list) == 1:
            double_check1 = input("Do you really want to delete? (Y/N): ")
            if double_check1 == "Y":
                asList.remove(deleting_list[0])
        else:
            for j in deleting_list:
                print(j)

            double_check2 = int(input("Choose which one to delete (1 for 1st row, 2 for 2nd row..etc): "))

            asList.remove(deleting_list[double_check2-1])

# Save the new lists over the existed one.

        adding_change = open("addressbook.csv","w",newline = "")
        adding = csv.writer(adding_change)
        adding.writerows(asList)

        mybook.close()
        adding_change.close()


# Modifiying the selected information when menu = 4
    elif menu == 4:
        mybook = open("addressbook.csv","r",newline = "")

        mydict = {"Name":"Enter the name to find which to modify : ",
                "Phone":"Enter the number to find which to modify : ",
                "Age":"Enter the age to find which to modify : ",
                "Address":"Enter the to find which to modify : "}


        mybook = open("addressbook.csv","r",newline = "")
        searching = csv.reader(mybook)
        asList = list(searching)
        header = asList[0]

        category = input("Select searching method (Name/Phone/Age/Address): ")
        details = input(mydict[category])
        myindex = header.index(category)

        modifying_list = []

        for each_info in asList:
            if str(each_info[myindex]) == details:
                modifying_list.append(each_info)
        # modifying_list = [each_info if str(each_info[myindex]) == details for each_info in asList]

        if len(modifying_list) == 0:
            print("No information found")

        else:
            newName = input("Enter New Name: ")
            newNum = int(input("Enter New Phone Number: "))
            newAge = int(input("Enter New Age: "))
            newAddress = input("Enter New Address: ")
            new_info = [newName,newNum,newAge,newAddress]

            if len(modifying_list) == 1:
                modifying_index = asList.index(modifying_list[0])
                asList[modifying_index] = new_info

            else:
                for j in modifying_list:
                    print(j)

                double_check1 = int(input("Choose which one to modify (1 for 1st row, 2 for 2nd row..etc): "))

                modifying_index = asList.index(modifying_list[double_check1-1])
                asList[modifying_index] = new_info

# Save the new lists over the existed one.

        adding_change = open("addressbook.csv","w",newline = "")
        adding = csv.writer(adding_change)
        adding.writerows(asList)

        mybook.close()
        adding_change.close()


# Print all information when menu = 5
    elif menu == 5:
        mybook = open("addressbook.csv","r",newline = "")
        reading = csv.reader(mybook)
        for eachrow in reading:
            print(eachrow)

    return True


def main():

    # Check if there already is the csv file, otherwise the existed information will be gone everytime you run it
    checking = os.path.isfile("addressbook.csv")

    if checking == False:
    # Creating new csv file if there hasn't been made one.
    # Adding header for my csv file
        mybook = open("addressbook.csv","w",newline = "")
        book_obj = csv.writer(mybook)
        book_obj.writerow(["Name","Phone","Age","Address"])
        mybook.close()

    keep_going = True

    while keep_going == True:
        print("1. Add information",
         "\n2. Searh information",
         "\n3. Delete information",
         "\n4. Modify information",
         "\n5. Print all information",
         "\n0. Exit")

        num = int(input("Enter your Menu number: "))


        keep_going = phonebook(num)




if __name__ == "__main__":
    main()
