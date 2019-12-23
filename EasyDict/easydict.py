class EasyDict(object):
    def __init__(self, init={}, normalize=False, **kwargs):
        self._normalize = normalize
        for key, value in init.items():
            self[key] = value
        for key, value in kwargs.items():
            self[key] = value

    def normalize(self, key):
        if self._normalize:
            return key.replace(" ", "_")
        return key

    def __getitem__(self, key):
        return self.__dict__[self.normalize(key)]

    def __setitem__(self, key, value):
        self.__dict__[self.normalize(key)] = value

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False

    def get(self, key, default=None):
        return self.__dict__.get(self.normalize(key), default)


if __name__ == '__main__':
    person = EasyDict(name="Trey Hunner", location="San Diego")
    # person = EasyDict({'name': "Trey Hunner", 'location': "San Diego"})
    print(person.name)
    print(person['location'])
