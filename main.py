class Currency:
    currencies = {
        'CHF': 0.930023,  # Swiss franc
        'CAD': 1.264553,  # Canadian dollar
        'GBP': 0.737414,  # British pound
        'JPY': 111.019919,  # Japanese yen
        'EUR': 0.862361,  # Euro
        'USD': 1.0  # US dollar
    }

    def __init__(self, value, unit="USD"):
        self.value = value
        self.unit = unit

    def changeTo(self, new_unit):
        """
        An Currency object is transformed from the unit "self.unit" to "new_unit"
        """
        if self.unit == new_unit:
            return self
        new_value = self.value / Currency.currencies[self.unit] * Currency.currencies.get(new_unit, 1.0)
        return Currency(new_value, new_unit)

    def __repr__(self):
        return f"{self.value:.2f} {self.unit}"

    def __add__(self, other):
        if isinstance(other, Currency):
            return Currency(self.value + other.changeTo(self.unit).value, self.unit)
        elif isinstance(other, (int, float)):
            return Currency(self.value + other, self.unit)
        else:
            raise TypeError("Unsupported operand type(s) for +: '{}' and '{}'".format(type(self), type(other)))

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, Currency):
            return Currency(self.value - other.changeTo(self.unit).value, self.unit)
        elif isinstance(other, (int, float)):
            return Currency(self.value - other, self.unit)
        else:
            raise TypeError("Unsupported operand type(s) for -: '{}' and '{}'".format(type(self), type(other)))

    def __rsub__(self, other):
        if isinstance(other, (int, float)):
            return Currency(other - self.value, self.unit)
        else:
            raise TypeError("Unsupported operand type(s) for -: '{}' and '{}'".format(type(self), type(other)))

v1 = Currency(23.43, "EUR")
v2 = Currency(19.97, "USD")
print(v1 + v2)
print(v2 + v1)
print(v1 + 3)
print(3 + v1)
print(v1 - 3)
print(30 - v2)