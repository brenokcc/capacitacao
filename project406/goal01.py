import json
import traceback
from datetime import datetime
from http import HTTPStatus


class WidgetException(Exception):
    message = 'Generic Widget exception.'
    http_status = HTTPStatus.INTERNAL_SERVER_ERROR

    def __init__(self, *args, customer_message=None):
        super().__init__(*args)
        if args:
            self.message = args[0]
        self.customer_message = customer_message if customer_message is not None else self.message

    @property
    def traceback(self):
        return traceback.TracebackException.from_exception(self).format()

    def log_exception(self):
        exception = {
            "type": type(self).__name__,
            "message": self.message,
            "args": self.args[1:],
            "traceback": list(self.traceback)
        }
        log = 'EXCEPTION: {}: {}'.format(datetime.utcnow().isoformat(), exception)
        print(log)
        return log

    def to_json(self):
        data = {
            'code': self.http_status.value,
            'message': '{}: {}'.format(self.http_status.phrase, self.customer_message),
            'category': type(self).__name__,
            'time_utc': datetime.utcnow().isoformat()
        }
        return json.dumps(data)


class SupplierException(WidgetException):
    message = 'Supplier exception'
    http_status = HTTPStatus.INTERNAL_SERVER_ERROR


class NotManufacturedException(SupplierException):
    message = 'Widget is no longer manufactured by supplier'
    http_status = HTTPStatus.INTERNAL_SERVER_ERROR


class ProductionDelayedException(SupplierException):
    message = 'Widget production has been delayed by supplier'
    http_status = HTTPStatus.INTERNAL_SERVER_ERROR


class ShippingDelayedException(SupplierException):
    message = 'Widget shipping has been delayed by supplier'
    http_status = HTTPStatus.INTERNAL_SERVER_ERROR


class CheckoutException(WidgetException):
    message = 'Checkout exception'
    http_status = HTTPStatus.INTERNAL_SERVER_ERROR


class InventoryException(CheckoutException):
    message = 'Checkout inventory exception'
    http_status = HTTPStatus.INTERNAL_SERVER_ERROR


class OutOfStockException(InventoryException):
    message = 'Inventory out of stock'
    http_status = HTTPStatus.INTERNAL_SERVER_ERROR


class PricingException(CheckoutException):
    message = 'Checkout pricing exception'
    http_status = HTTPStatus.INTERNAL_SERVER_ERROR


class InvalidCouponCodeException(PricingException):
    message = 'Invalid checkout coupon code'
    http_status = HTTPStatus.BAD_REQUEST


class CannotStackCouponException(PricingException):
    message = 'Cannot stack checkout coupon codes'
    http_status = HTTPStatus.BAD_REQUEST
