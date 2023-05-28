
class IDIterator:
    """
    A class used Iterate through IDs to find valid ones.
    """

    def __init__(self, id):
        self._id = id
        self._cur_id = id

    def __iter__(self):
        return self

    def next(self):
        """Get the next valid ID after _id, or the last ID returned.
            :return: The next valid ID.
            :rtype: int
            :raise: StopIteration: raises an Exception if out of bounds
            """
        while not check_id_valid(self._cur_id):
            if self._cur_id > 999999999:
                raise StopIteration
            self._cur_id += 1
        #Increase by one so it doesn't get stuck on this value every next.
        self._cur_id += 1
        return self._cur_id - 1



def check_id_valid(id_number):
    """Check if the ID is valid based on certain criterias.
        :param id_number: The ID which is need to be checked.
        :type id_number: int
        :return: If the sum of all the numbers is dividable by 10 after all the arithmetic methods on the ID digits.
        :rtype: bool
        """
    list_of_digits = [int(x) for x in str(id_number)]

    #Multiply the digits based on if they are even(*2) or odd(*1)
    for i in range(len(list_of_digits)):
        list_of_digits[i] = list_of_digits[i] * (2 ** (i % 2))

    #Merge number digits if he is bigger than 9.
    for i in range(len(list_of_digits)):
        if list_of_digits[i] > 9:
            list_of_digits[i] = list_of_digits[i] % 10 + int(list_of_digits[i] / 10)

    #Return if the sum of the digits is dividable by 10 at the end.
    return sum(list_of_digits) % 10 == 0

def id_generator (id_number):
    """Get the next valid ID after id_number, or the last ID returned.
        :param id_number: The ID which is need to be checked.
        :type id_number: int
        :return: The next valid ID.
        :rtype: int
        """
    while id_number < 999999999:
        if check_id_valid(id_number):
            yield id_number
        id_number += 1



def main():
    print(check_id_valid(123456780))
    print(check_id_valid(123456782))

    #Enter ID and Method
    id = int(input("Enter ID: "))
    method = input("Generator or Iterator? (gen/it)? ")

    if method == "it":
        #With Iterator
        id_iterator = IDIterator(id)
        if check_id_valid(id):
            next(id_iterator)
        for i in range(10):
            print(next(id_iterator))
    elif method == "gen":
        #With Generator
        id_gen = id_generator(id)
        if check_id_valid(id):
            next(id_gen)
        for i in range(10):
            print(next(id_gen))

if __name__ == "__main__":
    main()