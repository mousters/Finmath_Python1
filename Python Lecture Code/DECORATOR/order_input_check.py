class Order:
    __order_counter = 0
    def __init__(self, side, q, ticker, price, stamp, otype):
        self.side = side
        self.quantity = q
        self.ticker = ticker
        self.price = price
        self.timestamp = stamp
        self.order_type = otype
        self.__orderid = self.__assign_next_orderid()

    def update_order(self, **kwargs):
        if len(kwargs) == 0:
            raise Exception()
        else:
            self.price = kwargs.get('price', self.price)
            self.quantity = kwargs.get('quantity', self.quantity)
            self.order_type = kwargs.get('order_type', self.order_type)

    def process_order(self):
        print('This order is being processed')
        return True

    def __repr__(self):
        return '%s(side=%s, quantity=%d, ticker=\'%s\', price=%s, timestamp=%.3f, order_type=\'%s\')' % (
        self.__class__.__name__, self.side, self.quantity, self.ticker, self.price, self.timestamp, self.order_type)

    def __assign_next_orderid(self):
        Order.__order_counter += 1
        return Order.__order_counter

    @property
    def orderid(self):
        return self.__orderid

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, p):
        if p <= 0:
            raise Exception('Error: price %s <= 0' % p)
        else:
            self.__price = p

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, q):
        if not isinstance(q, int):
            raise Exception('Error: %s not of type int' % q)
        elif q <= 0:
            raise Exception('Error: quantity %s <= 0' % q)
        else:
            self.__quantity = q


class OptionOrder(Order):
    def __init__(self, side, q, ticker, price, stamp, otype, underlying_price, strike_price, expiration):
        super().__init__(side, q, ticker, price, stamp, otype)
        self.strike_price = strike_price
        self.expiration = expiration
        self.underlyling_price = underlying_price


class FutureOrder(Order):
    def __init__(self, side, q, ticker, price, stamp, otype, underlying_price, expiration):
        super().__init__(side, q, ticker, price, stamp, otype)
        self.expiration = expiration
        self.underlyling_price = underlying_price