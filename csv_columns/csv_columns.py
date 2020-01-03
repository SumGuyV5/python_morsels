import csv


def old_csv_columns(file, headers=None, missing=None):
    rtn = {}
    if headers:
        for header in headers:
            rtn[header] = []
    reader = csv.reader(file)
    for row in reader:
        if not rtn:
            for header in row:
                rtn[header] = []
        else:
            for header, column in zip(rtn, row):
                if not column:
                    column = missing
                rtn[header].append(column)
    return rtn


def csv_columns(file, headers=None, missing=None):
    tmp = {}
    reader = csv.DictReader(file, fieldnames=headers, restval=missing)
    for row in reader:
        for header, value in row.items():
            if header not in tmp:
                tmp[header] = []
            tmp[header].append(value)

    return tmp


if __name__ == '__main__':
    print(csv_columns(open('test.csv'), missing='1'))
