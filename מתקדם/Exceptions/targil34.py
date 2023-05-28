# coding=utf-8
import re
import string

class UsernameContainsIllegalCharacter(Exception):
    '''
    This class is responsible to handle exceptions when the username contains an illegal character.
    '''
    def __init__(self, arg):
        self._arg = arg

    def __str__(self):
        for ch in self._arg:
            if ch in string.punctuation.replace("_", ""):
                forbidden = ch
        return "{} - The username contains an illegal character \"{}\" at index {}".format(self._arg, forbidden, str(self._arg).find(forbidden))

    def get_arg(self):
        return self._arg

class UsernameTooShort(Exception):
    '''
    This class is responsible to handle exceptions when the username is too short.
    '''
    def __init__(self, arg):
        self._arg = arg

    def __str__(self):
        return "Your username is too short. It should be a least 3 characters but yours is {}".format(self._arg)

    def get_arg(self):
        return self._arg

class UsernameTooLong(Exception):
    '''
    This class is responsible to handle exceptions when the username is too long.
    '''
    def __init__(self, arg):
        self._arg = arg

    def __str__(self):
        return "Your username is too long. It should be a most 16 characters but yours is {}".format(self._arg)

    def get_arg(self):
        return self._arg

class PasswordMissingCharacter(Exception):
    '''
    This class is responsible to handle exceptions when the password is missing a must character.
    '''
    def __init__(self, arg):
        self._arg = arg

    def __str__(self):
        return "{} - Your password is missing a must character.".format(self._arg)

    def get_arg(self):
        return self._arg

class MissingUpperCharacter(PasswordMissingCharacter):
    '''
    This class is responsible to handle exceptions when the password is missing a must character in detail.
    '''
    def __init__(self, arg):
        self._arg = arg

    def __str__(self):
        return super().__str__() + "(Uppercase)"

    def get_arg(self):
        return self._arg

class MissingLowerCharacter(PasswordMissingCharacter):
    '''
    This class is responsible to handle exceptions when the password is missing a must character in detail.
    '''
    def __init__(self, arg):
        self._arg = arg

    def __str__(self):
        return super().__str__() + "(Lowercase)"

    def get_arg(self):
        return self._arg

class MissingSpecialCharacter(PasswordMissingCharacter):
    '''
    This class is responsible to handle exceptions when the password is missing a must character in detail.
    '''
    def __init__(self, arg):
        self._arg = arg

    def __str__(self):
        return super().__str__() + "(Special)"

    def get_arg(self):
        return self._arg

class MissingDigitCharacter(PasswordMissingCharacter):
    '''
    This class is responsible to handle exceptions when the password is missing a must character in detail.
    '''
    def __init__(self, arg):
        self._arg = arg

    def __str__(self):
        return super().__str__() + "(Digit)"

    def get_arg(self):
        return self._arg

class PasswordTooShort(Exception):
    '''
    This class is responsible to handle exceptions when the password is too short.
    '''
    def __init__(self, arg):
        self._arg = arg

    def __str__(self):
        return "Your password is too short. It should be a least 8 characters but yours is {}".format(self._arg)

    def get_arg(self):
        return self._arg

class PasswordTooLong(Exception):
    '''
    This class is responsible to handle exceptions when the password is too long.
    '''
    def __init__(self, arg):
        self._arg = arg

    def __str__(self):
        return "Your password is too long. It should be a most 16 characters but yours is {}".format(self._arg)

    def get_arg(self):
        return self._arg


def check_input(username, password):
    """Checks if the username and password are valid.
        :param username: The username of the user.
        :type username: str
        :param password: The password of the user.
        :type password: str
        :return: If the username and password are valid.
        :rtype: bool
        :raise: UsernameContainsIllegalCharacter: raises an Exception if username contains illegal character.
        :raise: UsernameTooShort: raises an Exception if username is too short.
        :raise: UsernameTooLong: raises an Exception if username is too long.
        :raise: PasswordMissingCharacter: raises an Exception if password is missing a character.
        :raise: MissingUpperCharacter: raises an Exception if password is missing an uppercase character.
        :raise: MissingLowerCharacter: raises an Exception if password is missing a lowercase character.
        :raise: MissingSpecialCharacter: raises an Exception if password is missing a special character.
        :raise: MissingDigitCharacter: raises an Exception if password is missing a digit character.
        :raise: PasswordTooShort: raises an Exception if password is too short.
        :raise: PasswordTooLong: raises an Exception if password is too long.
        """
    try:
        if re.search("[{}]".format(string.punctuation.replace("_", "")), username):
            raise UsernameContainsIllegalCharacter(username)
        elif len(username) < 3:
            raise UsernameTooShort(username)
        elif len(username) > 16:
            raise UsernameTooLong(username)
        elif not re.search("[a-z]", password):
            raise MissingLowerCharacter(password)
        elif not re.search("[A-Z]", password):
            raise MissingUpperCharacter(password)
        elif not re.search("[0-9]", password):
            raise MissingDigitCharacter(password)
        elif not re.search("[{}]".format(string.punctuation), password):
            raise MissingSpecialCharacter(password)
        elif len(password) < 8:
            raise PasswordTooShort(password)
        elif len(password) > 40:
            raise PasswordTooLong(password)
    except Exception as e:
        print(e)
        return False
    else:
        print("OK")
        return True






def main():
    check_input("1", "2")
    check_input("0123456789ABCDEFG", "2")
    check_input("A_a1.", "12345678")
    check_input("A_1", "2")
    check_input("A_1", "ThisIsAQuiteLongPasswordAndHonestlyUnnecessary")
    check_input("A_1", "abcdefghijklmnop")
    check_input("A_1", "ABCDEFGHIJLKMNOP")
    check_input("A_1", "ABCDEFGhijklmnop")
    check_input("A_1", "4BCD3F6h1jk1mn0p")
    check_input("A_1", "4BCD3F6.1jk1mn0p")

    username = input("Enter username: ")
    password = input("Enter password: ")
    while not check_input(username, password):
        username = input("Enter username: ")
        password = input("Enter password: ")



if __name__ == "__main__":
    main()