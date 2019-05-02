class Circle:


    def __init__(self,r):
        self.r = r



    def area(self):
        r = self.r
        
        A = 3.14*r*r

        return A

    def circumference(self):
        r = self.r
        C = 2*3.14*r

        return C



class Square:
    def __init__(self):
        self.a = a

    def area(self):
        a = self.a
        A = a*a

        return A

    def perimeter(self):
        a = self.a
        P = 4*a

        return P

class Rectangle:
    def __init__(self,w,l):
        self.w = w
        self.l = l

    def area(self):
        w = self.w
        l = self.l
        A = w*l

        return A

    def perimeter(self):
        w = self.w
        l = self.l
        P = 2*(w+l)

        return P


class Sphere:
    def __init__(self,r):
        self.r = r

    def surface_area(self):
        r = self.r
        SA = 4*3.14*r*r

        return SA

    def volume(self):
        r = self.r
        V = 4/3*3.14*r*r*r  

        return V                                      


