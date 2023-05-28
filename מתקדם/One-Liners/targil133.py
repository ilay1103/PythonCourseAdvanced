
def is_funny(string):
    return reduce(lambda x, y: x and y ,list(map(lambda x: str(x).lower() == 'h' or str(x).lower() == 'a', string)))

def main():
    print(is_funny("hahahahahaha"))



if __name__ == "__main__":
    main()