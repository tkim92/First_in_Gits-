class vec3:
    def __init__(self, mylist = [0,0,0]):
        self.lst = mylist

    def __str__(self):
        return str(self.lst)

    def vlist(self):
        return list(self.lst)

    def setValues(self,alist):
        self.lst = alist
        return self

    def magnitude(self):
        v_list = self.vlist()
        return float((v_list[0]**2 + v_list[1]**2 + v_list[2]**2)**(1/2))

    def sum_vector(self,rhand):
        list_1 = self.vlist()
        list_2 = rhand.vlist()
        return [list_1[0] + list_2[0]] + [list_1[1] + list_2[1]] + [list_1[2] + list_2[2]]

    # def division(self,rhand):
    #     list_1 = self.vlist()
    #     return [list_1[0] / rhand]  + [list_1[1] / rhand ] + [list_1[2] / rhand]

    def __truediv__(self,rhand):
        list_1 = self.vlist()
        return [list_1[0] / rhand]  + [list_1[1] / rhand ] + [list_1[2] / rhand]


def acceleration(force,mass):
    myforce = vec3(force)
    mag = myforce.magnitude()
    return mag / mass


# https://docs.python.org/3/reference/datamodel.html#special-method-names
