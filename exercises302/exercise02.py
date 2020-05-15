from datetime import datetime
from decimal import Decimal
from json import JSONDecoder, loads

from exercises302 import Stock, Trade


def decode_stock(data):
    return Stock(
        data['symbol'],
        datetime.strptime(data['date'], '%Y-%m-%d').date(),
        Decimal(data['open']),
        Decimal(data['high']),
        Decimal(data['low']),
        Decimal(data['close']),
        int(data['volume'])
    )


def decode_trade(data):
    return Trade(
        data['symbol'],
        datetime.strptime(data['timestamp'], '%Y-%m-%dT%H:%M:%S'),
        data['order'],
        Decimal(data['price']),
        int(data['volume']),
        Decimal(data['commission'])
    )


def decode(data):
    object_type = data.get('object', None)
    if object_type == 'Stock':
        return decode_stock(data)
    elif object_type == 'Trade':
        return decode_trade(data)
    return data


class CustomDecoder(JSONDecoder):
    def decode(self, s, **kwargs):
        return self.decode_recursively(loads(s))

    def decode_recursively(self, data):
        if isinstance(data, dict):
            data = decode(data)
            if isinstance(data, dict):
                for key, value in data.items():
                    data[key] = self.decode_recursively(value)
        elif isinstance(data, list):
            for index, item in enumerate(data):
                data[index] = self.decode_recursively(item)
        return data
