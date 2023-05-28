
class Dog:

    def __init__(self):
        self.name = "Butch"
        self.age = 0

    def birthday(self):
        self.age += 1

    def get_age(self):
        return self.age

def main():
    dog1 = Dog()
    dog2 = Dog()
    dog1.birthday()
    print (dog1.get_age())
    print (dog2.get_age())




if __name__ == "__main__":
    main()