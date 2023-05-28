def four_dividers(number):
    return list(filter(divder_of_four, range(1,number)))

def divder_of_four(number):
    return number % 4 == 0

def main():
    print(four_dividers(9))
    print(four_dividers(3))



if __name__ == "__main__":
    main()