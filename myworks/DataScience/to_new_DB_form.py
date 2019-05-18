
"""
Summary of this project.

We want to transform an existed data set into different form.
Detailed procedure is following:

1. We already have a data set witn 7 columns: (date, IP, attacker, victim, attack code, attack type, country)
2. Two main categories to compare: IP, attack type
3. Set a arbitrary variable to store updated data formatw
4. Check if the arbirary variable contains following:
      a) IP of the current data element
      b) Attack type of the current data element
5. If either(or both) of conditions in 4. is satisfied, append the corresponding information into
    the arbirary variable as a tuple
6. If the information is already present, leave them as it is. (only update with non - pre existed information)
7. If 4. is not satisfied, skip to next data element


Example:

mydata = (
            ("July", "IP1", "attacker1", "victim1", "code1", "type1", "USA")
            ("August", "IP3", "attacker1", "victim1", "code1", "type2", "USA")
            ("June", "IP2", "attacker1", "victim1", "code1", "type1", "USA")
            ("May", "IP2", "attacker1", "victim1", "code1", "type5", "USA")
        )
new_data = ()

-   Let the mydata[0] in new_data
-   mydata[1]'s IP/type: 'IP3' and 'type2'
-   new_data's IP/type: 'IP1' and 'type1'

-   4. is not satisfied -> move to mydata[2]

-   mydata[2]'s IP/type: 'IP2' and 'type1'
-   new_data's type is same as mydata[2]'s

-   updata new_data as following:
    new_Data = (("July","June"), ("IP1","IP2"), "attacker1", "victim1", "code1", "type1", "USA")

"""

def to_new_form(data):
    # Use list to take its advantage of being mutable.
    new_form = [[i] for i in data[0]]

    # Run for loop to meet two conditions:
    # Condition 1:  IP (index = 1) or Type (index = 5)
    # Condition 2: If condition 1 meets, ONLy new information is appended

    for i in range(len(data)):
        # condition 1
        if data[i][1] in new_form[1] or data[i][5] in new_form[5]:

            for j in range(7):
                # condition 2
                if data[i][j] not in new_form[j]:
                    new_form[j].append(data[i][j])

    return new_form




# Case 1: Either(or both) type,IP match
tu=(("20190129","dmz1","134.156.72.2","124.21.2.1","30010","php","한국"),
    ("20190310","dmz1","134.156.72.2","124.21.2.1","30010","php3","한국"),
    ("20190310", "test56", "134.156.73.2", "124.21.2.1", "30010", "php", "한국")
    )

As_tuple = tuple([tuple(k) for k in to_new_form(tu)])
print(As_tuple)
