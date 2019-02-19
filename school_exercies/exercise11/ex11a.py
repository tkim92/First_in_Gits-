class Vehicle:
    def __init__(self,mname,ncyl,owner):
        self.manufacturer_name = mname
        self.num_cylinders = ncyl
        self.owner = owner

    def getMname(self):
        return self.manufacturer_name

    def getNcyl(self):
        return self.num_cylinders

    def getOwner(self):
        return self.owner

class Truck(Vehicle):
    def __init__(self,mname,ncyl,owner,lcap,tcap):
        super().__init__(mname,ncyl,owner)
        self.load_capacity = lcap
        self.tow_capacity = tcap

    def getLcap(self):
        return self.load_capacity

    def getTcap(self):
        return self.tow_capacity

def main():
    car = Truck("honda",6,"TK",10,5)
    print(car.getLcap)
    print(car.getMname)
    print(car.getNcyl)
    print(car.getOwner)

if __name__ == "__main__":
    main()
