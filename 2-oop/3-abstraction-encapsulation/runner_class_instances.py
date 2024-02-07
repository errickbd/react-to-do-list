from class_instances import Circle, Dog


# No class instances at all
# print(Circle.PI)

my_circle = Circle(4)
# print(Circle.PI)
# print(my_circle.get_area())
# print(my_circle.get_circumfrence())

the_circle = Circle(2)
# print(the_circle.pi)
# print(the_circle.get_area())
# print(the_circle.get_circumfrence())


dog1 = Dog("Buddy", "Labrador")
dog2 = Dog("Miles", "Labrador")
print(dog1.describe_dog())
print(dog2.describe_dog())

Dog.SPECIES = "Space Dog!!"

print(dog1.describe_dog())
print(dog2.describe_dog())

Dog.toys.append('frisbee')
print(Dog.toys)