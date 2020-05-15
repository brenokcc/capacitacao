from datetime import date, datetime
from decimal import Decimal
from json import JSONEncoder

from exercises302 import Stock, Trade


class CustomEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Stock):
            return dict(
                symbol=obj.symbol,
                date=obj.date,
                open=obj.open,
                high=obj.high,
                low=obj.low,
                close=obj.close,
                volume=obj.volume,
                object='Stock'
            )
        if isinstance(obj, Trade):
            return dict(
                symbol=obj.symbol,
                timestamp=obj.timestamp,
                order=obj.order,
                price=obj.price,
                volume=obj.volume,
                commission=obj.commission,
                object='Trade'
            )
        elif isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%dT%H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        elif isinstance(obj, Decimal):
            return str(obj)
        else:
            return super().default(obj)
