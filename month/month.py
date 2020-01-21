import datetime
import calendar


class Month:
    #__slots__ = ['__year', '__month']

    def __init__(self, year, month):
        self.__year = year
        self.__month = month

    @property
    def year(self):
        return self.__year

    @property
    def month(self):
        return self.__month

    @property
    def first_day(self):
        return datetime.date(self.year, self.month, 1)

    @property
    def last_day(self):
        cal = calendar.monthrange(self.year, self.month)
        return datetime.date(self.year, self.month, cal[1])

    @classmethod
    def from_date(cls, date):
        return Month(date.year, date.month)

    def strftime(self, str):
        return self.first_day.strftime(str)

    def __str__(self):
        return f'{self.year}-{str(self.month).zfill(2)}'

    def __eq__(self, other):
        if isinstance(other, Month):
            return self.year == other.year and self.month == other.month
        return None

    def __le__(self, other):
        if isinstance(other, Month):
            if self.year < other.year:
                return True
            elif self.year == other.year:
                return self.month < other.month
            return False
        raise TypeError(f"TypeError: '>' not supported between instances of '{type(other)}' and 'Month'")

    def __gt__(self, other):
        if isinstance(other, Month):
            if self.year > other.year:
                return True
            elif self.year == other.year:
                return self.month > other.month
            return False
        raise TypeError(f"TypeError: '<' not supported between instances of 'Month' and '{type(other)}'")

    def __repr__(self):
        return f"Month({self.year}, {self.month})"

    def __hash__(self):
        return self.first_day.__hash__()


