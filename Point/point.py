class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.next = 0

    def __eq__(self, other):
        return (self.x, self.y, self.z) == (other.x, other.y, other.z)

    def __ne__(self, other):
        return (self.x, self.y, self.z) != (other.x, other.y, other.z)

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y}, z={self.z})"

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        z = self.z + other.z
        return Point(x, y, z)

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        z = self.z - other.z
        return Point(x, y, z)

    def __mul__(self, other):
        return Point(self.x * other, self.y * other, self.z * other)

    def __rmul__(self, other):
        return self * other

    def __divmod__(self, other):
        x = self.x / other
        y = self.y / other
        z = self.z / other
        return Point(x, y, z)

    def __iter__(self):
        val = [self.x, self.y, self.z]
        for i in val:
            yield i


if __name__ == "__main__":
    p1 = Point(1, 2, 3)
    p2 = Point(1, 2, 3)

    print(p1)