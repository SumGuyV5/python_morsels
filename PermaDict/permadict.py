DEFAULT = object()


class PermaDict(dict):
    def __delitem__(self, key):
        value = super().pop(key)
        super().pop(value, None)

    def __setitem__(self, key, value):
        if key in self:
            raise KeyError(f"'{key}' already in dictionary.")
        if value is self:
            del self[value]
        super().__setitem__(key, value)
        # super().__setitem__(value, key)

    def __repr__(self):
        return f"{type(self).__name__}({super().__repr__()})"

    def pop(self, key, default=DEFAULT):
        if key in self or default is DEFAULT:
            value = self[key]
            del self[key]
            return value
        else:
            return default

    """ def update(self, items):
        if isinstance(items, dict):
            items = items.items()
        for key, value in items:
            if key in self:
                raise KeyError(f"'{key}' already in dictionary.")
            else:
                self[key] = value"""

    def update(self, other=None, **kwargs):
        if isinstance(other, dict):
            for key, value in other.items():
                self[key] = value
        elif other is not None:
            for key, value in other:
                self[key] = value
        for key, value in kwargs.items():
            self[key] = value

    def force_set(self, key, value):
        if key in self:
            del self[self[key]]
        if value is self:
            del self[value]
        super().__setitem__(key, value)
        # super().__setitem__(value, key)


if __name__ == '__main__':
    locations = PermaDict({'Trey': "San Diego", 'Al': "San Francisco"})
    locations['Harry'] = "London"
    locations.update({'Russell': "Perth", 'Katie': "Sydney"})
    print(f"{locations['Trey']}")

    locations = PermaDict([('Kojo', "Houston"), ('Tracy', "Toronto")])
    print(f'{list(locations)}')
    d = PermaDict()
    d[4] = "the number four"
    print(f'{d.pop(4)}')

    for name, place in locations.items():
        print(f"{name} in {place}")

    locations = PermaDict({'David': "Boston"})
    # locations['David'] = "Amsterdam"

    locations['Asheesh'] = "Boston"
    locations.update({'Asheesh': "San Francisco"})

    for name, place in locations.items():
        print(f"{name} in {place}")
