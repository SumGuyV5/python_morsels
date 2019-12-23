import calendar
from enum import IntEnum
import datetime


class Weekday(IntEnum):
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6


def meetup_date(year, month, nth=4, weekday=Weekday.THURSDAY):
    c = calendar.monthcalendar(year, month)
    mod = -1
    if c[0][weekday] == 0 or nth < 0:
        mod = 0
    if nth < 0 and c[nth][weekday] == 0:
        mod = -1

    return datetime.date(year, month, c[nth + mod][weekday])


if __name__ == '__main__':
    print(meetup_date(2012, 3))
