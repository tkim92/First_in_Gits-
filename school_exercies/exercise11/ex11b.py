class Person:
    def __init__(self,name,address,pnumber,email):
        self.name = name
        self.address = address
        self.pnumber = pnumber
        self.email = email

    def __repr__(self):
        return self.name + " Person"

class Student(Person):
    def __init__(self,name,address,pnumber,email,status):
        """
        status: freshman, sophomore, junior, senior
        """
        super().__init__(name,address,pnumber,email)
        self.status = status

    def __repr__(self):
        return self.name + " Student"

class Employee(Person):
    def __init__(self,name,address,pnumber,email,office,salary,hiredate):
        super().__init__(name,address,pnumber,email)
        self.office = office
        self.salary = salary
        self.hiredate = hiredate

    def __repr__(self):
        return self.name  + " Employee"


class Faculty(Employee):
    def __init__(self,name,address,pnumber,email,office,salary,hiredate,officehour,rank):
        """
        Rank: assistant, associate, professor
        """
        super().__init__(name,address,pnumber,email,office,salary,hiredate)
        self.officehour = officehour
        self.rank = rank

    def __repr__(self):
        return self.name + " Faculty"

class Staff(Employee):
    def __init__(self,name,address,pnumber,email,office,salary,hiredate,title):
        super().__init__(name,address,pnumber,email,office,salary,hiredate)
        self.title = title

    def __repr__(self):
        return self.name + " Staff"

def main():
    p = Person("Taiwoo","Venue","911","umn.edu")
    s = Student("Taiwoo","Venue","911","umn.edu","senior")
    e = Employee("Taiwoo","Venue","911","umn.edu","Vincent 230","$80,000","18-03-01")
    f = Faculty("Taiwoo","Venue","911","umn.edu","Vincent 230","$80,000","18-03-01","04AM","Assistant")
    s = Staff("Taiwoo","Venue","911","umn.edu","Vincent 230","$80,000","18-03-01","ASA")

    print(p)
    print(s)
    print(e)
    print(f)
    print(s)

if __name__ == "__main__":
    main()
