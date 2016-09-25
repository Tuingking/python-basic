''' Object
=========================================================================================================
symbol "__" di "__name" menandakan private variable
'''

class Animal:
    __name = ""
    __height = 0
    __weight = 0
    __sound = ""

    def __init__(self, name, height, weight, sound):
        print("Animal Class")
        self.__name = name
        self.__height = height
        self.__weight = weight
        self.__sound = sound

    # setter
    def set_name(self, name):
        self.__name = name

    # getter
    def get_name(self):
        return self.__name

    def set_height(self, height):
        self.__height = height

    def get_height(self):
        return self.__height

    def set_weight(self, weight):
        self.__weight = weight

    def get_weight(self):
        return self.__weight

    def set_sound(self, sound):
        self.__sound = sound

    def get_sound(self):
        return self.__sound

    def get_type(self):
        print ("Animal")

    def toString(self):
        return "{} is {} cm tall and {} kg and say {}".format(self.__name,
                                                              self.__height,
                                                              self.__weight,
                                                              self.__sound)

# cat = Animal("Whiskers", 33, 10, "Meow")
# print (cat.toString())