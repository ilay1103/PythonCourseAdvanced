
def intersection(list_1, list_2):
    return [x for x in set(list_1) if x in set(list_2)]


def main():
    print(intersection([1, 2, 3, 4], [8, 3, 9]))
    print(intersection([5, 5, 6, 6, 7, 7], [1, 5, 9, 5, 6]))



if __name__ == "__main__":
    main()