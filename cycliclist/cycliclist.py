from itertools import cycle

class CyclicList(list):
    def __init__(self, items, start=0):
        self.items = items
        self.num = start
        self._data_len = len(items)

    def __iter__(self):
        return cycle(self.items)

    def __next__(self):
        nx = self.items[self.num]
        self.num += 1
        self.num %= len(self.items)
        return nx

    def __len__(self):
        return self._data_len

    def __getitem__(self, index):
        return self.items[index % len(self)]

    def __setitem__(self, index, value):
        self.items[index % len(self)] = value

    def pop(self, *args, **kwargs):
        return self.items.pop(*args, **kwargs)

    def append(self, item):
        self.items.append(item)
        self._data_len = len(self.items)




if __name__ == '__main__':
    test = CyclicList([1, 2, 3])
    for x in test:
        print(f'{x}')