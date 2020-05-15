from datetime import date, datetime
from decimal import Decimal
from json import dumps, loads

from exercises302 import Stock, Trade
from exercises302.exercise01 import CustomEncoder
from exercises302.exercise02 import CustomDecoder
from exercises302.exercise03 import TradeSchema, StockSchema, ActivitySchema

activity = {
    "quotes": [
        Stock('TSLA', date(2018, 11, 22), Decimal('338.19'), Decimal('338.64'), Decimal('337.60'), Decimal('338.19'),
              365_607),
        Stock('AAPL', date(2018, 11, 22), Decimal('176.66'), Decimal('177.25'), Decimal('176.64'), Decimal('176.78'),
              3_699_184),
        Stock('MSFT', date(2018, 11, 22), Decimal('103.25'), Decimal('103.48'), Decimal('103.07'), Decimal('103.11'),
              4_493_689)
    ],

    "trades": [
        Trade('TSLA', datetime(2018, 11, 22, 10, 5, 12), 'buy', Decimal('338.25'), 100, Decimal('9.99')),
        Trade('AAPL', datetime(2018, 11, 22, 10, 30, 5), 'sell', Decimal('177.01'), 20, Decimal('9.99'))
    ]
}

encoded = """{
  "quotes": [
    {
      "symbol": "TSLA",
      "date": "2018-11-22",
      "open": "338.19",
      "high": "338.64",
      "low": "337.60",
      "close": "338.19",
      "volume": 365607,
      "object": "Stock"
    },
    {
      "symbol": "AAPL",
      "date": "2018-11-22",
      "open": "176.66",
      "high": "177.25",
      "low": "176.64",
      "close": "176.78",
      "volume": 3699184,
      "object": "Stock"
    },
    {
      "symbol": "MSFT",
      "date": "2018-11-22",
      "open": "103.25",
      "high": "103.48",
      "low": "103.07",
      "close": "103.11",
      "volume": 4493689,
      "object": "Stock"
    }
  ],
  "trades": [
    {
      "symbol": "TSLA",
      "timestamp": "2018-11-22T10:05:12",
      "order": "buy",
      "price": "338.25",
      "volume": 100,
      "commission": "9.99",
      "object": "Trade"
    },
    {
      "symbol": "AAPL",
      "timestamp": "2018-11-22T10:30:05",
      "order": "sell",
      "price": "177.01",
      "volume": 20,
      "commission": "9.99",
      "object": "Trade"
    }
  ]
}"""


def test_custom_encode():
    result = dumps(activity, cls=CustomEncoder, indent=2)
    assert result == encoded


def test_cusom_decode():
    decoded = loads(encoded, cls=CustomDecoder)
    for i, stock in enumerate(decoded['quotes']):
        assert activity['quotes'][i] == stock
    for i, trade in enumerate(decoded['trades']):
        assert activity['trades'][i] == trade


def test_stock_schema():
    result = StockSchema().dumps(
        Stock('TSLA', date(2018, 11, 22), Decimal('338.19'), Decimal('338.64'), Decimal('337.60'), Decimal('338.19'),
              365_607)
    )
    decoded = '{"volume": 365607, "open": "338.19", "high": "338.64", "low": "337.60", "close": "338.19", "symbol": ' \
              '"TSLA", "date": "2018-11-22"}'
    assert loads(result) == loads(decoded)


def test_trade_schema():
    result = TradeSchema().dumps(
        Trade('TSLA', datetime(2018, 11, 22, 10, 5, 12), 'buy', Decimal('338.25'), 100, Decimal('9.99'))
    )
    decoded = '{"volume": 100, "price": "338.25", "timestamp": "2018-11-22T10:05:12", "symbol": "TSLA", ' \
              '"commission": "9.99", "order": "buy"}'
    assert loads(result) == loads(decoded)


def test_activity_schema():
    result = ActivitySchema().dumps(activity)
    print(result)


test_custom_encode()
test_cusom_decode()
test_stock_schema()
test_trade_schema()
test_activity_schema()
