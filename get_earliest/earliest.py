from datetime import datetime


def date_sort(date):
    m, d, y = date.split('/')
    return y, m, d


def get_earliest(*dates):
    return min(dates, key=date_sort)


if __name__ == "__main__":
    print(get_earliest("01/27/1832", "01/27/1756"))
