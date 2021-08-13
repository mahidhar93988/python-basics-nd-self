# Your class should be named as `Rectangle`.
# Method to get area should be named as `rectangle_area`.
# Method to get perimeter should be named as `rectangle_perimeter`.
# You should be taking `length` and `width` as inputs when creating the object for your class.

class Rectangle():
    def __init__(self, l, b):
        self.l = l
        self.w = b

    def rectangle_area(self):
        if(self.l <= 0 or self.w <= 0):
            return(0)
        return(self.l*self.w)

    def rectangle_perimeter(self):
        if(self.w <= 0 or self.l <= 0):
            return(0)
        return(2*(self.w+self.l))


if __name__ == "__main__":
    newRectangle = Rectangle(int(input()), int(input()))
    print(newRectangle.rectangle_area())
    print(newRectangle.rectangle_perimeter())
