def gen_secs():
    #Get seconds from 0-59
    x = 0
    while True:
        yield x % 60
        x += 1

def gen_minutes():
    #Get minutes from 0-59
    x = 0
    while True:
        yield x % 60
        x += 1

def gen_hours():
    #Get hours from 0-23
    x = 0
    while True:
        yield x % 24
        x += 1

def gen_time():
    hours = gen_hours()
    minutes = gen_minutes()
    seconds = gen_secs()

    for second in seconds:
        if second == 0:
            minute = next(minutes)
            if minute == 0:
                hour = next(hours)
        #Returns the time in the format, also returns a bool value if its the and of the day.
        yield ("%02d:%02d:%02d" % (hour, minute, second), (second == 59 and minute == 59 and hour == 23))



def gen_years(start=2023):
    #Get year each time
    while True:
        yield start
        start += 1

def gen_months():
    #Get months from 1-12
    x = 0
    while True:
        yield (x % 12) + 1
        x += 1

def gen_days(month, leap_year=True):
    #Get days based on the month and if its a leap year.
    months = {1:31, 2:(28 + int(leap_year)), 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    return (i for i in range(1, months[month] + 1))

def gen_date():
    years = gen_years()
    months = gen_months()

    year = next(years)
    for month in months:
        for day in gen_days(month, (year % 4 == 0 and (year % 400 == 0 or year % 100 != 0))):
            for time, is_new_day in gen_time():
                if not is_new_day:
                    yield "%02d/%02d/%04d %s" % (day, month, year, time)
                else:
                    #Break if we need to move to a new day
                    break
        if month == 12:
            year = next(years)

def main():

    i = 0
    for date in gen_date():
        if i % 1000000 == 0:
            print(date)
        i += 1


if __name__ == '__main__':
    main()