"""
Write a Python class Rectangle with:

Private attributes for length and width
Methods to calculate area (getArea()) and perimeter getPerimeter())
A method to check if it's a square (isSquare())

"""
class Rectangle :
    def __init__(self,length,width):
        self.__length = length
        self.__width = width

    def getArea(self):
        return f"area of {self.__length*self.__width},length{self.__length},width{self.__width}"
    def getPerimeter(self):
        return f"Paramiter is {2*(self.__length*self.__width)}"   
    def isSquare(self):
        return self.__length == self.__width

myrectangle = Rectangle(10,5)
print(f"Area is {myrectangle.getArea()}")
print(f"Parameter is {myrectangle.getPerimeter()}")
print(f"Square is {myrectangle.isSquare()}")