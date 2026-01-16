'''
Simple Class Practice
Create a class called 'Rectangle':
__init__ takes length and width
Method: area() - returns area
Method: perimeter() - returns perimeter
Method: is_square() - returns True if length == width

Create 3 Rectangle objects and test all methods.
'''

class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width

    def area(self):
        areaFormula=self.width*self.length
        return f'Area Of Rectangle {areaFormula}'
    
    def perimeter(self):
        perimeterFormula=2*(self.width+self.length)
        return f'Perimeter Of Rectangle {perimeterFormula}'

    def is_square(self):
        if(self.length==self.width):
            return f'length and width are same'
        else:
            return f'length and width are not same'

cal=Rectangle(4,5)
print(cal.area())
print(cal.perimeter())
print(cal.is_square())

    


        