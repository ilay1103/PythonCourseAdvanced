import itertools


def main():
    wallet = [20, 20, 20, 10, 10, 10, 10, 10, 5, 5, 1, 1, 1, 1, 1]
    combinations = set()
    for amount in range(1, len(wallet) + 1):
        combinations.update(itertools.combinations(wallet, amount))

    for combination in combinations:
        if sum(combination) == 100:
            print(combination)

if __name__ == '__main__':
    main()