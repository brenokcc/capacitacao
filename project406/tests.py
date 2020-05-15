from project406.goal01 import InvalidCouponCodeException

e = InvalidCouponCodeException('User tried to use an old coupon', customer_message='Sorry. This coupon has expired')


def test_log_exception():
    log = ": {'type': 'InvalidCouponCodeException', 'message': 'User tried to use an old coupon', 'args': (), " \
          "'traceback': ['project406.goal01.InvalidCouponCodeException: User tried to use an old coupon\\n']}"
    assert e.log_exception().endswith(log)


def test_to_json():
    json = '{"code": 400, "message": "Bad Request: Sorry. This coupon has expired", "category": ' \
           '"InvalidCouponCodeException", "time_utc": '
    assert e.to_json().startswith(json)


test_log_exception()
test_to_json()

