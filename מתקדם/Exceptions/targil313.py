# coding=utf-8

'''ImportError'''
import stam

def main():
    '''StopIteration'''
    nums = [1, 2, 3, 4, 5]
    my_iter = iter(nums)
    while True:
        item = next(my_iter)
        print(item)

    '''ZeroDivisionError'''
    print(3 / 0)

    '''AssertionError'''
    assert 0 != 0

    '''KeyError'''
    ages = {}
    ages[3]

    '''SyntaxError'''
    while True
        print "HI"

    '''IndentationError'''
        print(3)

    '''TypeError'''
    print(3 + '3')

if __name__ == "__main__":
    main()