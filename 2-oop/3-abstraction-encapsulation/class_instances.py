
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

    def how_many_legs(self):
        return Dog.LEGS

    def describe_dog(self):
        return f"My name is {self.name}, I am a {self.breed} of {Dog.SPECIES} with {Dog.LEGS}"

class Circle:
    PI = 3.14159

    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return Circle.PI * (self.radius^2)


    def  get_circumfrence(self):
        return 2 * Circle.PI * self.radius
    