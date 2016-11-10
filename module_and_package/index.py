from myModule import Person
from myPackage.car import *

import sys

person1 = Person()
person1.name = "Yoko"
person1.say_hello()

myCar = Car()
myCar.setSpeed(100)

myTruck = Truck()
myTruck.setSpeed(70)

print ("sys version: {}".format(sys.version))