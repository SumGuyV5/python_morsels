import re
import sys

date_reg_exp = re.compile('(\d+[-/]\d+[-/]\d+\n)')

def entries_by_date(file):
    rtn = []
    text = ""
    for line in file:
        text += line.replace('&quot;', '"').replace('&nbsp;', ' ').replace('&amp;', '&')

    matches_list = date_reg_exp.findall(str(text))
    for match in matches_list:
        rtn.append(match.rstrip())
        print(f'{match}')

    for i in range(0, len(rtn)):
        idx = len(text)
        text = text.split(rtn[i], 1)[1].lstrip()
        if i < len(rtn) - 1:
            idx = text.index(rtn[i + 1])

        rtn[i] = (rtn[i], text[0:idx].lstrip().rstrip())
        text = text[idx:len(text)]

    return rtn


def main(text):
    f = open(text, 'r')
    result = entries_by_date(f)

    for date, entry in result:
        f = open(f'{date}.txt', 'w')
        f.writelines(entry)
        f.close()


if __name__ == '__main__':
    text = """2018-01-01
    
Coded.&quot;

Did laundry.

2018-01-02

Slept all day."""
    print(f'{entries_by_date(text)}')
