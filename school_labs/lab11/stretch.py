class measure:
    def __init__(self,feet = 0, inches = None):
        if inches == None:
            self.inches = feet
            self.feet = 0
            if feet >= 12:
                self.feet = feet // 12
                self.inches = feet % 12
        else:
            if inches < 12:
                self.feet = feet
                self.inches = inches
            else:
                self.feet = inches // 12 + feet
                self.inches = inches % 12

    def __str__(self):
        if self.feet == 0 and self.inches == 0:
            return str(0) + '"'
        elif self.feet != 0 and self.inches == 0:
            return str(self.feet) + "' "
        else:
            return str(self.feet) + "' " + str(self.inches) + '"'

    def __add__(self,rhand):
        return measure(self.feet + rhand.feet,self.inches + rhand.inches)

    def __sub__(self,rhand):
        sub_m = measure(self.feet - rhand.feet,self.inches - rhand.inches)
        if sub_m.inches < 0:
            sub_m.feet = sub_m.feet -1
            sub_m.inches = sub_m.inches + 12
            return sub_m
        return sub_m
