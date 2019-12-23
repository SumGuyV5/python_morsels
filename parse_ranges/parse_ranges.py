import re

def parse_ranges(ranges):
    for ran in ranges.split(","):
        start, sep, end = ran.partition('-')
        end = re.sub("[^0-9]", "", end)
        if not end:
            end = start
        for i in range(int(start), int(end) + 1):
            yield i

if __name__ == "__main__":
    r = parse_ranges('0-0, 4-8, 20->end, 43-45')
    #r = parse_ranges('1-2,4-4,8-10')
    print(r)