# area_perimeter_circle


class Circle:
    def __init__(self, r):
        self.rad = r

    def getArea(self):
        if(self.rad <= 0):
            return(0.0)
        return(3.14*self.rad**2)

    def getCircumference(self):
        if(self.rad <= 0):
            return(0.0)
        return(2*3.14*self.rad)


if __name__ == "__main__":
    one_circle = Circle(float(input()))
    print(float(one_circle.getArea()))
    print(float(one_circle.getCircumference()))
