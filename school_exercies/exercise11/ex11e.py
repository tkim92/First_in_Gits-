class Vehicle:
    def __init__(self,make,model,year,mileage,price):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage
        self.price = price

    def setMake(self,make):
        self.make = make

    def setModel(self,model):
        self.model = model

    def setYear(self,year):
        self.year = year

    def setMileage(self,mileage):
        self.mileage = mileage

    def setPrice(self,price):
        self.price = price


    def getMake(self):
        return self.make

    def getModel(self):
        return self.model

    def getYear(self):
        return self.year

    def getMileage(self):
        return self.mileage

    def getPrice(self):
        return self.price

    def Display(self):
        mk = "Make: " + str(self.getMake())
        yr = "Year: " + str(self.getYear())
        mo = "Model: " + str(self.getModel())
        mi = "Miles: " + str(self.getMileage())
        pr = "Price: " + str(self.getPrice())

        for i in (mk,yr,mo,mi,pr):
            print(i)

class Car(Vehicle):
    # door: number of doors
    def __init__(self,make,model,year,mileage,price,door):
        super().__init__(make,model,year,mileage,price)
        self.door = door

    def setDoor(self,door):
        self.door = door

    def getDoor(self):
        return self.door

    def Display(self):
        print("Inventory unit: Car")
        super().Display()
        print("Number of doors: " + str(self.getDoor()))


    # type: 2 wheel drive or 4 wheel drive
class Truck(Vehicle):
    def __init__(self,make,model,year,mileage,price,type):
        super().__init__(make,model,year,mileage,price)
        self.type = type

    def setType(self,type):
        self.type = type

    def getType(self):
        return self.type

    def Display(self):
        print("Inventory unit: Truck")
        super().Display()
        print("Drive Type: " + str(self.getType()))


    # capacitiy = passenger Capacity
class SUV(Vehicle):
    def __init__(self,make,model,year,mileage,price,capacity):
        super().__init__(make,model,year,mileage,price)
        self.capacity = capacity

    def setCapacity(self,capacity):
        self.capacity = capacity

    def getCapacity(self):
        return self.capacity

    def Display(self):
        print("Inventory unit: SUV")
        super().Display()
        print("Passenger Capacity: " + str(self.getCapacity()))

class Inventory:
    def __init__(self):
        self.mlist = []

    # The argument, vehicle, is an obect
    def addVehicle(self,vehicle):
        self.mlist.append(vehicle)

    def Display(self):
        for i in self.mlist:
            i.Display()
            print("\n")

def main():

    cont = "Y"

    while cont == "Y":
        type = input("Enter your vehicle type: ")
        make = input("Enter your vehicle make: ")
        model = input("Enter your vehicle model: ")
        year = input("Enter your vehicle year: ")
        mile = input("Enter your vehicle mileage: ")
        price = input("Enter your vehicle price: ")

        if type == "Car" or "car":
            door = input("Enter your number of doors: ")
            # addition = door
        elif type == "Truck" or "truck":
             drive_type = input("Enter your vehicle drive type: ")
             # addition = drive_type
        elif type == "SUV" or "suv":
             cap = input("Enter your passenger capacity: ")
             # addition = cap

        types = ["car","truck","suv"]
        for j in range(0,3):
            if type.lower() == types[j]:
                if j == 0:
                    avehicle = Car(make,model,year,mile,price,door)
                elif j == 1:
                    avehicle = Truck(make,model,year,mile,price,drive_type)
                elif j == 2:
                    avehicle = SUV(make,model,year,mile,price,cap)
        it = Inventory()
        it.addVehicle(avehicle)

        cont = "Add another vehicle (Y/N): "

    it.Display()

if __name__ == "__main__":
    main()
