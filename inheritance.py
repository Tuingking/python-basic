from class_object import Animal

''' Inheritance
=========================================================================================================
symbol "__" di "__name" menandakan private variable
'''

class Dog(Animal):
    __owner = ""

    def __init__(self, name, height, weight, sound, owner):
        print ("Dog Class")
        self.__owner = owner
        super(Dog, self).__init__(name, height, weight, sound)

    def set_owner(self, owner):
        self.__owner = owner

    def get_owner(self):
        return self.__owner

    def get_type(self):
        print ("Dog")

    def toString(self):
        return "{} is {} cm tall and {} kg and say {}, his owner is {}".format(self.get_name(),
                                                                               self.get_height(),
                                                                               self.get_weight(),
                                                                               self.get_sound(),
                                                                               self.__owner)

    def multiple_sound(self, how_many=None):
        if how_many is None:
            print(self.get_sound())
        else:
            print(self.get_sound() * how_many)

# spot = Dog("Spot", 170, 100, "Guk", "Molly")
# print (spot.toString())
# spot.multiple_sound(10)