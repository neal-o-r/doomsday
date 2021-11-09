from collections import namedtuple

Date = namedtuple("Date", ["day", "month", "year"], defaults=[None]*3)

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

doomsdays = [
    (14, 3),
    (4, 4),
    (9, 5),
    (6, 6),
    (11, 7),
    (8, 8),
    (5, 9),  # 9-5 @ 7-11
    (10, 10),
    (7, 11),
    (26, 12),
]
# doomsdays in [1600, 1700, ...] were on day of week index:
century_dooms = [1, 2, 4, 6]


def get_input():
    dt = input("Input a date: (dd.mm.yyyy)\n")
    return Date(*map(int, dt.split(".")))


def is_leap_year(year):
    mod4 = year % 4 == 0
    mod100 = year % 100 != 0
    mod400 = year % 400 == 0
    return (mod4 & mod100) | mod400


def get_dooms(date):
    leap = is_leap_year(date.year)
    return [Date(d, m) for d, m in [(3 + leap, 1), (28 + leap, 2)] + doomsdays]


def algorithm(date):

    dooms = get_dooms(date)

    century = date.year // 100
    year = date.year % 100

    # get the doomsday for that century
    century_offset = century_dooms[(16 - century) % 4]

    # then add the year offset (with leap years)
    year_offset = year + year // 4

    # get the day offset from the nearest doomsday
    day_offset = next(date.day - d.day for d in dooms if d.month == date.month)

    offset = century_offset + year_offset + day_offset

    return days[offset % 7]


def main():
    print(algorithm(get_input()))
