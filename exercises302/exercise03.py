from marshmallow import Schema, fields
from marshmallow import post_load

from exercises302 import Stock, Trade


class StockSchema(Schema):
    symbol = fields.Str()
    date = fields.Date()
    open = fields.Decimal(as_string=True)
    high = fields.Decimal(as_string=True)
    low = fields.Decimal(as_string=True)
    close = fields.Decimal(as_string=True)
    volume = fields.Integer()

    @post_load()
    def make_stock(self, data):
        return Stock(**data)


class TradeSchema(Schema):
    symbol = fields.Str()
    timestamp = fields.DateTime()
    order = fields.Str()
    price = fields.Decimal(as_string=True)
    commission = fields.Decimal(as_string=True)
    volume = fields.Integer()

    @post_load
    def make_trade(self, data):
        return Trade(**data)


class ActivitySchema(Schema):
    trades = fields.Nested(TradeSchema, many=True)
    quotes = fields.Nested(StockSchema, many=True)
