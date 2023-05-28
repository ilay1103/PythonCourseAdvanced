# coding=utf-8

def read_file(file_name):
    """Reads from the file.
        :param file_name: The file path to be read.
        :type file_name: str
        :return: The content of the file.
        :rtype: str
        """
    file_content = "__CONTENT_START__"
    try:
        file_content += '\n'
        file = open(file_name, 'r')
    except Exception:
        file_content += "__NO_SUCH_FILE__\n"
    else:
        file_content += file.read() + '\n'
    finally:
        file_content += "__CONTENT_END__"
        return file_content

def main():
    print(read_file("one_lined_file.txt"))
    print(read_file("file_does_not_exist.txt"))


if __name__ == "__main__":
    main()