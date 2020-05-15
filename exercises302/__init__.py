"""
Coding Exercises
Consider the following classes:
"""


class Stock:
    def __init__(self, symbol, date, open_, high, low, close, volume):
        self.symbol = symbol
        self.date = date
        self.open = open_
        self.high = high
        self.low = low
        self.close = close
        self.volume = volume

    def __repr__(self):
        return "Stock('{}', {}, Decimal('{}'), Decimal('{}'), Decimal('{}'), Decimal('{}'), {})".format(
            self.symbol, self.date, self.open, self.high, self.low, self.close, self.volume
        )

    def __eq__(self, other):
        return self.__repr__() == other.__repr__()


class Trade:
    def __init__(self, symbol, timestamp, order, price, volume, commission):
        self.symbol = symbol
        self.timestamp = timestamp
        self.order = order
        self.price = price
        self.commission = commission
        self.volume = volume

    def __repr__(self):
        return "Trade('{}', {}, '{}', Decimal('{}'), 20, Decimal('{}'))".format(
            self.symbol, self.timestamp, self.order, self.price, self.commission
        )

    def __eq__(self, other):
        return self.__repr__() == other.__repr__()


"""
Exercise 1
Given the above class, write a custom JSONEncoder class to serialize dictionaries that contain instances of these particular classes. Keep in mind that you will want to deserialize the data too - so you will need some technique to indicate the object type in your serialization.

Exercise 2
Write code to reverse the serialization you just created. Write a custom decoder that can deserialize a JSON structure containing Stock and Trade objects.

Exercise 3
Do the same serialization and deserialization, but using Marshmallow.
"""