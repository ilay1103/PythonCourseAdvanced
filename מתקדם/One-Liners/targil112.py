def double_letter(my_str):
    return "".join(list(map(double, my_str)))

def double(letter):
    return letter * 2

def main():
    my_str = "python"
    print(double_letter(my_str))



if __name__ == "__main__":
    main()