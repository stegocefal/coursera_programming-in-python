class Pet:
    def __init__(self, name=None):
        print('This is __init__ from "Pet" class.')
        self.name = name


class Dog(Pet):
    def __init__(self, name, breed=None):
        self.name = name
        self.breed = breed

    def say(self):
        return "{0}: waw".format(self.name)


class WoolenDog(Dog):
    def __init__(self, name, breed=None):
        # явное указание метода конкретного класса
        super(Dog, self).__init__(name)
        self.breed = "Шерстяная собака породы {0}".format(breed)


woolenDog = WoolenDog('Name', 'Breed')
