
class BigThing:

    def __init__(self, val):
        self._val = val


    def size(self):
        if isinstance(self._val, int):
           return self._val
        else:
           return len(self._val)


class BigCat(BigThing):

    def __init__(self,val , weight):
        BigThing.__init__(self, val)
        self._weight = weight


    def size(self):
        if self._weight > 20:
           return "Very Fat"
        elif self._weight > 15:
            return "Fat"
        else:
           return "OK"



def main():
    my_thing = BigThing("balloon")
    print(my_thing.size())
    my_thing = BigThing(6)
    print(my_thing.size())
    my_thing = BigThing([3,2])
    print(my_thing.size())
    cutie = BigCat("mitzy", 22)
    print(cutie.size())
    cutie = BigCat("mitzy", 7)
    print(cutie.size())
    cutie = BigCat("mitzy", 18)
    print(cutie.size())





if __name__ == "__main__":
    main()