"""
Composition vs Inheritance

Composition:
    - Composition is "Has-a" Relationship
        - Ex: Car HAS wheels, Car HAS Engine
    - What is it? 
        - Using multiple classes together without inheritance.
    - Advantages:
        - Flexibility

Inheritance:
    - Inheritance is "Is-a" relationship
        - Truck IS a type of Car
        - Dog IS an Animal
    - What is it?
        - Using inheritance (parent / child classes) to share common logic & behavior amongst classes.
    - Advantages
        - Establish relationships
        - More code resuse, structure and hierarchy
"""









class Engine:
    def start(self):
        return "Engine started"

class Wheel: 
    def rotate(self):
        return "Wheel rotated"

class FourWheeledMotorVehicle:
    def __init__(self):
        self.engine = Engine()
        # python fanciness to get a list of 4 wheels
        # self.wheels = [Wheel(), Wheel(), Wheel(), Wheel()]
        self.wheels = [Wheel() for _  in range(4)]

    def start(self):
        return self.engine.start()

    def drive(self):
        return "Car is driving"

car1 = FourWheeledMotorVehicle()
car1.start()
car1.drive()

class Truck(FourWheeledMotorVehicle):
    def __init__(self):
        super().__init__()
        self.stuff_in_truck_bed = []

    def put_in_truck_bed(self, item):
        self.put_in_truck_bed.append(item)

class Sedan(FourWheeledMotorVehicle):
    def __init__(self):
        pass

    def open_trunk(self):
        return "Trunk is open"

class Van(FourWheeledMotorVehicle):
    def __init__(self):
        pass

    def open_sliding_door(self):
        return "Sliding door open"

my_truck = Truck()
# print(my_truck.start())
# print(my_truck.wheels[1].rotate())











# Example of composition
class Aviary:
    def __init__(self, birds=[]):
        self.birds = birds

    def add_bird(self, bird):
        self.birds.append(bird)

class Bird:
    aviary = Aviary()
    def __init__(self, name):
        self.name = name
        Bird.aviary.add_bird(self)

    def __repr__(self):
        return f"{self.name}"

my_aviary = Aviary()
tweety = Bird("tweety")
fido = Bird("iago")
# print(my_aviary.birds)
# main.py

# Polymorphism
# The same interface for different classes


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} says Meow!"


class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    pass

class Duck(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        return f"Quack! Says {self.name}"

duck1 = Duck("Tim Robins")
print(duck1.speak())

# cat1 = Cat()
# print(cat1.speak())

# dog1 = Dog()
# print(dog1.speak())

# bestiary = [duck1, cat1, dog1]

# for some_animal in bestiary:
    # print(some_animal.speak())

    # Polymorphism with an abstract base class
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass # Abstract method for all shapes

    @abstractmethod
    def circumfrence(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def circumfrence(self):
        return self.width * 2 + self.height * 2

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

# my_shape = Shape() # Doesn't exist

my_rect = Rectangle(4, 5)
print(my_rect.circumfrence())
print(my_rect.area())