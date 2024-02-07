from string_utils import StringUtils
import Math




print(Math.floor(3.141))





print(StringUtils.is_palindrome("racecar"))

class Circle:
    PI = 3.14159

    @staticmethod
    def calculate_diameter(radius):
        return radius * 2

    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return Circle.PI * self.radius ** 2

    def get_diameter(self):
        return Circle.calculate_diameter(self.radius)

circle = Circle(5)
print(circle.calculate_area())  # Output: 78.53975


# Example of Class Methods in action
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    @classmethod
    def create_square(cls, side_length): 
        return cls(side_length, side_length) # Rectangle(side_length, side_length)

    def __str__(self):
        return f"Width: {self.width} | Height: {self.height}"

rectangle1 = Rectangle(5, 20)
rectangle2 = Rectangle(5, 2)
print(rectangle2)
square = Rectangle.create_square(4) # create_square(Rectangle, 4)
print(square)

class Dog:
    LEGS = 4
    SPECIES = "Dog species"
    toys = [
        'stick', 
        'ball'
    ]

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    @staticmethod
    def animal_info():
        return f"Species: {Dog.SPECIES} | # of legs: {Dog.LEGS}."

    @classmethod
    def create_labrador(cls, name):
        return cls(name, "Labrador Retriever")

    @classmethod
    def create_poodle(cls, name):
        return cls(name, "Poodle")

    def how_many_legs(self):
        return Dog.LEGS

    def describe_dog(self):
        return f"My name is {self.name}, I am a {self.breed} of {Dog.SPECIES} with {Dog.LEGS}"

    def __str__(self):
        return self.describe_dog()




fido = Dog.create_labrador("Fido")
print(fido)
arthur = Dog.create_poodle("Arthur")
print(arthur)

print(Dog.animal_info())