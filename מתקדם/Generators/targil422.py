
def parse_ranges(ranges_string):
    ranges = (str(i).split('-') for i in str(ranges_string).split(','))
    numbers = []
    for start, stop in ranges:
        for num in range(int(start), int(stop) + 1):
            numbers.append(num)
    return numbers

def main():
    print(list(parse_ranges("1-2,4-4,8-10")))
    print(list(parse_ranges("0-0,4-8,20-21,43-45")))

if __name__ == '__main__':
    main()