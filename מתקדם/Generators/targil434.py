def get_fibo():
    x = 0
    y = 1
    while True:
        yield x
        x += y
        yield y
        y += x

def main():
    fibo_gen = get_fibo()
    print(next(fibo_gen))
    print(next(fibo_gen))
    print(next(fibo_gen))
    print(next(fibo_gen))


if __name__ == '__main__':
    main()