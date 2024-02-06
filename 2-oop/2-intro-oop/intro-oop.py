# Everything in Python is an object. And every object is an instance of some class
# print(type(True))
# print(type(None))
# print(type(3))
# print(type('hello'))
# print(type([]))

# Doing exact change problem in an object oriented way
class Denomination:
    def __init__(self, value, singular, plural):
        self.value = value
        self.singular = singular
        self.plural = plural

penny = Denomination(.01, "penny", "pennies")

six_pennies = AmountDenomination(6, penny)
# print(six_pennies.message())

dollar = Denomination(1, "dollar bill", "dollar bills")

five_bucks = AmountDenomination(5, dollar)
# print(five_bucks.denomination.value)
# print(five_bucks.denomination.singular)
# print(five_bucks.message())

# print(penny.value)
# print(penny.singular)
# print(penny.plural)
# print(type(dollar))
# print(type(penny))

# Define a class named Dog
class Dog:
    # class constructor method, aka init method
    def __init__(self, doggie_name, breed, color, sound):
        print(f"doggies name: {doggie_name}")
        self.name = doggie_name
        self.breed = breed
        self.color = color
        self.sound = sound

    # print(fido) calls this
    # str(fido) calls this
    def __str__(self):
        return f"I am a {self.color} {self.breed} dog named {self.name} and I say {self.sound}"

    # need this if we want info on our class to be printed when its an item in a list
    def __repr__(self):
        return str(self)

    def speak(self):
        print(f"Doggo says {self.sound}")

    def fetch(self, item="ball"):
        print(f"{self.name} fetched the {item}")

    def speak_and_fetch(self, item="ball"):
        self.speak()
        self.fetch(item)

# Create an instance of the dog class
fido = Dog("Fido", "Pointer", "white", "bark!")
# print(type(fido))
# fido.speak()
# fido.fetch("stick")
# fido.speak_and_fetch()

# print(fido)

alfred = Dog("Alfred", "Golden Retriever", "Golden", "woof!")
# alfred.speak_and_fetch("stick")

# print(alfred)
# print([fido, alfred])

# Inheritance
class Mammal:
    def __init__(self, species, is_aquatic=False):
        self.species = species
        self.is_aquatic = is_aquatic

    def say_hi(self):
        print(f"Hi! I am a {self.species}")

    def __str__(self):
        return f"Mammal {self.species} is aquatic: {self.is_aquatic}"

    def declare_am_mammal(self):
        print("I am a mammal")

class Cat(Mammal):
    def __init__(self, is_aquatic=False):
        super().__init__("Cat", is_aquatic)


class Dolphin(Mammal):
    def __init__(self, is_aquatic=True):
        super().__init__("Dolphin", is_aquatic)

    def echolocation(self):
        print("squeak!")

my_cat = Cat()
my_cat.declare_am_mammal()
print(my_cat)
my_cat.say_hi()

flipper = Dolphin()
flipper.echolocation()

# Two levels of inheritance gets tricky. Generally, avoid it
# NOTE: Bugs/issues here
class CheshireCat(Cat):
    def __init__(self, name, species, is_aquatic=False):
        super().__init__(species, is_aquatic)
        self.name = name

    def say_hi(self):
        print("I am special I'm from Alice in Wonderland")

    def disappear(self, name):
        print(f"{self.name} disappears")


# special_cat = CheshireCat("Alice in wonderland cat", "Cat")

