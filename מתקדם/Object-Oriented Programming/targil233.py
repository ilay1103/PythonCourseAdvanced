
class Dog:

    count_animals = 0

    def __init__(self, name = "Octavio"):
        self._name = name
        self._age = 0
        Dog.count_animals += 1

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def birthday(self):
        self._age += 1

    def get_age(self):
        return self._age

def main():
    dog1 = Dog("Butch")
    dog2 = Dog()
    print (dog1.get_name())
    print (dog2.get_name())
    dog2.set_name("Barak")
    print (dog2.get_name())
    print (Dog.count_animals)





if __name__ == "__main__":
    main()