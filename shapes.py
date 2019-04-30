class Circle:


    def __init__(self,radius):
        self.radius = 0



    def area(self,r):
        
        A = 3.14*r*r

        return A

    def circumference(self,r):
        C = 2*3.14*r

        return C



class Square:
    def __init__(self,a):
        self.a = 0

    def area(self,a):
        A = a*a

        return A

    def perimeter(self,a):
        P = 4*a

        return P

class Rectangle:
    def __init__(self,w,l):
        self.w = 0
        self.l = 0

    def area(self,w,l):
        A = w*l

        return A

    def perimeter(self,w,l):
        P = 2*(w+l)

        return P


class Sphere:
    def __init__(self,r):
        self.r = 0

    def surface_area(self,r):
        SA = 4*3.14*r*r

        return SA

    def volume(self,r):
        V = 4/3*3.14*r*r*r  

        return V                                      


