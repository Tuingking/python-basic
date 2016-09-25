from class_object import Animal
from inheritance import Dog

''' Polymorphism
=========================================================================================================
'''

class AnimalTesting:
    def __init__(self):
        print ("AnimalTesting Class")

    def get_type(self, animal):
        animal.get_type()

cat = Animal("Whiskers", 33, 10, "Meow")
spot = Dog("Spot", 170, 100, "Guk", "Molly")

test_animals = AnimalTesting()
test_animals.get_type(cat)
test_animals.get_type(spot)