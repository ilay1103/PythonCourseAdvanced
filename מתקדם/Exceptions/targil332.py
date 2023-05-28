# coding=utf-8

class UnderAge(Exception):
    '''
    This class is responsible to handle exceptions when the person is under-age
    '''
    def __init__(self, arg):
        self._arg = arg

    def __str__(self):
        return "You are younger than 18 years old. " \
               "\nYour age is {}, and you need to wait {} years in order to be invited.".format(self._arg, 18-self._arg)

    def get_arg(self):
        return self._arg


def send_invitation(name, age):
    """Sends invitation to guests.
        :param name: The name of the guest to be invited.
        :type name: str
        :param age: The age of the guest to be invited.
        :type age: int
        :return:
        :rtype: None
        :raise: UnderAge: raises an Exception if the guest we want to invite is under-age
        """
    try:
        if int(age) < 18:
            raise UnderAge(age)
    except UnderAge as e:
        print(e)
    else:
        print("You should send an invite to " + name)

def main():
    send_invitation("Idan", 17)
    send_invitation("Ilay", 20)


if __name__ == "__main__":
    main()