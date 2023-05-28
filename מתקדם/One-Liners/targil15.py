import functools

def longest_name(file_path):
    with open(file_path, 'r') as file:
        print(reduce(lambda x,y: x if len(x) > len(y) else y, file.read().split('\n')))

def total_length_names(file_path):
    with open(file_path, 'r') as file:
        print(reduce(lambda x,y: x + len(y), file.read().split('\n'), 0))

def shortest_names(file_path):
    with open(file_path, 'r') as file:
        lines = file.read().split('\n')
        print('\n'.join(filter(lambda x: len(x) == reduce(lambda x,y: x if x < len(y) else len(y), lines, reduce(lambda x, y: x if x > len(y) else len(y), lines, 0)), lines)))

def write_name_lengths(file_path):
    with open(file_path, 'r') as file:
        with open(r"name_length.txt", "w") as write_file:
            map(lambda x: write_file.write(str(len(x))+'\n'), file.read().split('\n'))

def names_in_length(file_path, length):
    with open(file_path, 'r') as file:
        print('\n'.join(filter((lambda x: len(x) == length), file.read().split('\n'))))

def main():
    file_path = r"names.txt"
    longest_name(file_path)
    total_length_names(file_path)
    shortest_names(file_path)
    write_name_lengths(file_path)
    names_in_length(file_path, int(input("Enter name length you'd like: ")))





if __name__ == "__main__":
    main()