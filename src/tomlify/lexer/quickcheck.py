class Outer:
    def __init__(self, x):
        print(f"Initializing Outer with x = {x}")
        self._x = x

    @property
    def x(self):
        x = self._x
        print(f"Getting Outer x: {x}")
        return x

    @x.setter
    def x(self, value):
        print(f"Setting Outer x: {value}")
        self._x = value

class Inner:
    def __init__(self, outer):
        print("Initializing Inner")
        self._outer = outer

    @property
    def x(self):
        x = self._outer.x
        print(f"Getting Inner x: {x}")
        return x

    @x.setter
    def x(self, value):
        print(f"Setting Inner x: {value}")
        self._outer.x = value

outer = Outer(1)
inner = Inner(outer)

print(outer.x)
print(inner.x)

inner.x = 2

print(outer.x)
print(inner.x)
