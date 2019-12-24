def sum_timestamps(lst):
    hours = 0
    min = 0
    sec = 0
    for time in lst:
        x = time.split(':')
        sec += int(x[-1])

        if len(x) > 1:
            min += int(x[-2])
        if len(x) > 2:
            hours += int(x[-3])


    m, s = divmod(sec, 60)
    sec = s
    min += m
    h, m = divmod(min, 60)
    min = m
    hours += h
    if hours <= 0:
        return f'{min}:{sec:02d}'
    else:
        return f'{hours}:{min:02d}:{sec:02d}'

if __name__ == '__main__':
    times = [
        '3:52', '3:29', '3:23', '4:05', '3:24', '2:29', '2:16', '2:44',
        '1:58', '3:21', '2:51', '2:53', '2:51', '3:32', '3:20', '2:40',
        '2:50', '3:24', '1:20', '3:22', '3:26', '0:42', '5:20']
    print(f"{sum_timestamps(times)}")