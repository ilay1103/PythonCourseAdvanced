import file2

def main():
    greeting = file2.GreetingCard()
    birthday = file2.BirthdayCard()

    greeting.greeting_msg()
    birthday.greeting_msg()


if __name__ == '__main__':
    main()