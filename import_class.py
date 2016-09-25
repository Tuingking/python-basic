# Import class Animal from class_object.py
from class_object import Animal
cat = Animal("Whiskers", 33, 10, "Meow")
print (cat.toString())

print("\n"*2)

# Import class Dog from inheritance.py
from inheritance import Dog
spot = Dog("Spot", 170, 100, "Guk", "Molly")
print (spot.toString())
spot.multiple_sound(10)