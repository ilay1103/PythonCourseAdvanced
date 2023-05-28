# coding=utf-8
class Animal:
    '''
    This class represents animals in general.
    '''
    zoo_name = "Hayaton"

    def __init__(self, name, hunger = 0):
        self._name = name
        self._hunger = hunger

    def get_name(self):
        '''Returns the Animal's name
        	   :param self: The instance of the animal.
        	   :type self: instance.
        	   :return: The name.
        	   :rtype: str.
        	   '''
        return self._name


    def is_hungry(self):
        '''Returns if the Animal is hungry.
                :param self: The instance of the animal.
                :type self: instance.
                :return: If hunger is bigger than zero.
                :rtype: bool.
                '''
        return self._hunger > 0

    def feed(self):
        '''Feeds the animal(Decreases hunger by one).
                :param self: The instance of the animal.
                :type self: instance.
                :return:
                :rtype: None.
                '''
        self._hunger -= 1

    def talk(self):
        '''Lets the animal talk.
                :param self: The instance of the animal.
                :type self: instance.
                :return:
                :rtype: None.
                '''
        pass


class Dog(Animal):
    '''
    This class represents dogs.
    '''
    def __init__(self, name, hunger = 0):
        Animal.__init__(self, name, hunger)

    def talk(self):
        '''Lets the dog talk.
                :param self: The instance of the animal.
                :type self: instance.
                :return:
                :rtype: None.
                '''
        print("woof woof")

    def fetch_stick(self):
        '''The dog fetches a stick.
                :param self: The instance of the animal.
                :type self: instance.
                :return:
                :rtype: None.
                '''
        print("There you go, sir!")


class Cat(Animal):
    '''
    This class represents cats.
    '''
    def __init__(self, name, hunger = 0):
        Animal.__init__(self, name, hunger)

    def talk(self):
        '''Lets the cat talk.
                :param self: The instance of the animal.
                :type self: instance.
                :return:
                :rtype: None.
                '''
        print("meow")

    def chase_laser(self):
        '''The cat chases a lazer.
                :param self: The instance of the animal.
                :type self: instance.
                :return:
                :rtype: None.
                '''
        print("Meeeeow")


class Skunk(Animal):
    '''
    This class represents skunks.
    '''
    def __init__(self, name, hunger = 0, stink_count = 6):
        Animal.__init__(self, name, hunger)
        self._stink_count = stink_count

    def talk(self):
        '''Lets the skunk talk.
                :param self: The instance of the animal.
                :type self: instance.
                :return:
                :rtype: None.
                '''
        print("tsssss")

    def stink(self):
        '''The stunk sprays his stinky liquid.
                :param self: The instance of the animal.
                :type self: instance.
                :return:
                :rtype: None.
                '''
        print("Dear lord!")


class Unicorn(Animal):
    '''
    This class represents unicorns.
    '''
    def __init__(self, name, hunger = 0):
        Animal.__init__(self, name, hunger)

    def talk(self):
        '''Lets the unicorn talk.
                :param self: The instance of the animal.
                :type self: instance.
                :return:
                :rtype: None.
                '''
        print("Good day, darling")

    def sing(self):
        '''The unicorns starts to sing.
                :param self: The instance of the animal.
                :type self: instance.
                :return:
                :rtype: None.
                '''
        print("I’m not your toy...")


class Dragon(Animal):
    '''
    This class represents dragons.
    '''
    def __init__(self, name, hunger = 0, color = "Green"):
        Animal.__init__(self, name, hunger)
        self._color = color

    def talk(self):
        '''Lets the dragon talk.
                :param self: The instance of the animal.
                :type self: instance.
                :return:
                :rtype: None.
                '''
        print("Raaaawr")

    def breath_fire	(self):
        '''The dragon breathes his fire.
                :param self: The instance of the animal.
                :type self: instance.
                :return:
                :rtype: None.
                '''
        print("$@#$#@$")




def main():
    zoo_lst = list()
    zoo_lst.append(Dog("Brownie", 10))
    zoo_lst.append(Cat("Zelda", 3))
    zoo_lst.append(Skunk("Stinky", 0))
    zoo_lst.append(Unicorn("Keith", 7))
    zoo_lst.append(Dragon("Lizzy", 1450))

    zoo_lst.append(Dog("Doggo", 80))
    zoo_lst.append(Cat("Kitty", 80))
    zoo_lst.append(Skunk("Stinky Jr.", 80))
    zoo_lst.append(Unicorn("Clair", 80))
    zoo_lst.append(Dragon("McFly", 80))

    for animal in zoo_lst:
        print("{}: {}".format(animal.__class__.__name__, animal.get_name()))
        while animal.is_hungry():
            animal.feed()
        animal.talk()
        if isinstance(animal, Dog):
            animal.fetch_stick()
        elif isinstance(animal, Cat):
            animal.chase_laser()
        elif isinstance(animal, Skunk):
            animal.stink()
        elif isinstance(animal, Unicorn):
            animal.sing()
        elif isinstance(animal, Dragon):
            animal.breath_fire()
    print(Animal.zoo_name)




if __name__ == "__main__":
    main()