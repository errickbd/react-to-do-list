class Animal:
    def __init__(self, species, breed, name, sound): 
        self.species = species
        self.name = name
        self.breed = breed
        self.sound = sound

    def __str__(self):
        return f"Species: {self.species} | Breed: {self.breed} | Name: {self.name}"

    def make_sound(self):
        print(f"{self.sound}")














class Dog(Animal):
    def __init__(self, breed, name, is_a_big_dog):
        super().__init__("Dog", breed, name, "bark!")

        self.is_a_big_dog = is_a_big_dog

    def roll_over(self):
        print(f"{self.name} rolls over and waits for a treat")

    def dances(self):
        print(f"{self.name} dances and waits for a treat")

fido = Dog("labrador", "fido", True)
noodles = Dog("poodle", "poodle", False)
fido.make_sound()
noodles.make_sound()
# print(fido)
# fido.roll_over()
# fido.bark()
# print(noodles)
# noodles.roll_over()
# noodles.bark()










class Cat(Animal):
    def __init__(self, breed, name):
        super().__init__("Feline", breed, name, "meow...")
        self.litterbox = 0

    def use_litterbox(self):
        print(f"{self.name} uses litterbox like a good cat")
        self.litterbox += 1 
        print(f"litterbox uses {self.litterbox}")

        if self.litterbox >= 3:
            print(f"{self.name} says the litterbox is dirty")

    def clean_litterbox(self):
        print("Owner cleans litterbox")
        self.litterbox = 0

garfield = Cat("Orange", "Garfield", )
garfield.make_sound()
# print(garfield)

# garfield.use_litterbox()
# garfield.use_litterbox()
# garfield.use_litterbox()
# garfield.use_litterbox()
# garfield.clean_litterbox()
# garfield.use_litterbox()



