import time
from enum import Enum

import unittest
class OrderType(Enum):
    LIMIT = 1
    MARKET = 2
    IOC = 3


class OrderSide(Enum):
    BUY = 1
    SELL = 2


class NonPositiveQuantity(Exception):
    pass

class NonPositivePrice(Exception):
    pass

class InvalidSide(Exception):
    pass

class UndefinedOrderType(Exception):
    pass

class UndefinedOrderSide(Exception):
    pass

class NewQuantityNotSmaller(Exception):
    pass

class UndefinedTraderAction(Exception):
    pass

class UndefinedResponse(Exception):
    pass

from abc import ABC

class Order(ABC):
    def __init__(self, id, symbol, quantity, side, time):
        self.id = id
        self.symbol = symbol
        if quantity > 0:
            self.quantity = quantity
        else:
            raise NonPositiveQuantity("Quantity Must Be Positive!")
        if side in [OrderSide.BUY, OrderSide.SELL]:
            self.side = side
        else:
            raise InvalidSide("Side Must Be Either \"Buy\" or \"OrderSide.SELL\"!")
        self.time = time

class LimitOrder(Order):
    def __init__(self, id, symbol, quantity, price, side, time):
        super().__init__(id, symbol, quantity, side, time)
        self.type=OrderType.LIMIT
        if price > 0:
            self.price = price
        else:
            raise NonPositivePrice("Price Must Be Positive!")
        self.type = OrderType.LIMIT

class MarketOrder(Order):
    def __init__(self, id, symbol, quantity, side, time):
        super().__init__(id, symbol, quantity, side, time)
        self.type = OrderType.MARKET

class IOCOrder(Order):
    def __init__(self, id, symbol, quantity, price, side, time):
        super().__init__(id, symbol, quantity, side, time)
        if price > 0:
            self.price = price
        else:
            raise NonPositivePrice("Price Must Be Positive!")
        self.type = OrderType.IOC

class FilledOrder(Order):
    def __init__(self, id, symbol, quantity, price, side, time, limit=False):
        super().__init__(id, symbol, quantity, side, time)
        self.price = price
        self.limit = limit
        self.side=side
import operator

class MatchingEngine():
    def __init__(self):
        self.bid_book = []
        self.ask_book = []
        # These are the order books you are given and expected to use for matching the orders below

    def handle_order(self, order):
        if order.type == OrderType.LIMIT:
            return self.handle_limit_order(order)
        elif order.type == OrderType.MARKET:
            return self.handle_market_order(order)
        elif order.type == OrderType.IOC:
            return self.handle_ioc_order(order)
        else:
            raise UndefinedOrderType("Undefined Order Type!")

    def sort_order(self):
        self.bid_book = sorted(self.bid_book, key=lambda o: (-o.price, o.time))
        self.ask_book = sorted(self.ask_book, key=lambda o: (o.price, o.time))
    def handle_buy(self,order):
        filled_orders=[]
        removal=[]
        if len(self.ask_book) == 0 and order.type == OrderType.LIMIT:
            self.insert_limit_order(order)
            return
        for e in self.ask_book:
            # print('matching engine', e.quantity, order.quantity)
            #e for existing order
            if order.quantity==0:
                break
            elif order.type==OrderType.LIMIT:
                if e.quantity> order.quantity and e.price<=order.price:
                    # print('C1', order.id)
                    # print(e.quantity,order.quantity)
                    e.quantity-=order.quantity
                    filled_orders.append(FilledOrder(e.id, e.symbol, order.quantity, e.price, e.side, e.time))
                    filled_orders.append(FilledOrder(order.id,order.symbol,order.quantity,e.price,order.side,order.time))
                    order.quantity = 0
                    break
                elif  e.quantity<= order.quantity and e.price<=order.price:
                    # print('C2')
                    filled_orders.append(FilledOrder(e.id,e.symbol,e.quantity,e.price,e.side,e.time))
                    filled_orders.append(FilledOrder(order.id, e.symbol, e.quantity, e.price, order.side, order.time))
                    order.quantity -= e.quantity
                    # print('filled order len ',len(filled_orders))
                    removal.append(e)
                    if order.quantity==0:
                        break
                elif e.price > order.price and order.quantity>0:
                    self.insert_limit_order(order)
            elif order.type==OrderType.MARKET:
                if e.quantity>order.quantity:
                    e.quantity-=order.quantity
                    filled_orders.append(FilledOrder(order.id, order.symbol, order.quantity, e.price, order.side, order.time))
                    filled_orders.append(FilledOrder(e.id, e.symbol, e.quantity, e.price, e.side, e.time))
                    break
                elif e.quantity<= order.quantity:
                    order.quantity -= e.quantity
                    filled_orders.append(FilledOrder(e.id, e.symbol, e.quantity, e.price, e.side, e.time))
                    removal.append(e)
                    if order.quantity == 0:
                        filled_orders.append(FilledOrder(order.id, order.symbol, e.quantity, e.price, order.side, order.time))
                        break
            elif order.type==OrderType.IOC:
                if e.quantity> order.quantity and e.price<=order.price:
                    e.quantity-=order.quantity
                    filled_orders.append(FilledOrder(order.id,order.symbol,order.quantity,e.price,order.side,order.time))
                    filled_orders.append(FilledOrder(e.id, e.symbol, e.quantity, e.price, e.side, e.time))
                    break
                elif  e.quantity<= order.quantity and e.price<=order.price:
                    order.quantity-=e.quantity
                    filled_orders.append(FilledOrder(e.id,e.symbol,e.quantity,e.price,e.side,e.time))
                    removal.append(e)
                    if order.quantity==0:
                        filled_orders.append(FilledOrder(order.id, order.symbol, e.quantity, e.price, order.side, order.time))
                        break
        for i in removal:
            self.ask_book.remove(i)
        if order.quantity>0 and order.type==OrderType.LIMIT:
            self.insert_limit_order(order)
        return filled_orders

    def handle_sell(self,order):
        filled_orders = []
        removal=[]
        if len(self.bid_book)==0 and order.type==OrderType.LIMIT:
            self.insert_limit_order(order)
            return
        for e in self.bid_book:
            # e for existing order
            if order.quantity == 0:
                break
            elif order.type == OrderType.LIMIT:
                if e.quantity > order.quantity and e.price >= order.price:
                    # print('C1',order.id)
                    # print(e.quantity, order.quantity)
                    e.quantity -= order.quantity
                    filled_orders.append(FilledOrder(e.id, e.symbol, order.quantity, e.price, e.side, e.time))
                    filled_orders.append(FilledOrder(order.id, order.symbol, order.quantity, e.price, order.side, order.time))
                    order.quantity = 0
                    break
                elif e.quantity <= order.quantity and e.price >= order.price:
                    # print('C2')
                    filled_orders.append(FilledOrder(e.id, e.symbol, e.quantity, e.price, e.side, e.time))
                    filled_orders.append(FilledOrder(order.id, e.symbol, e.quantity, e.price, order.side, order.time))
                    order.quantity -= e.quantity
                    removal.append(e)
                    if order.quantity == 0:
                        # filled_orders.append(FilledOrder(order.id, order.symbol, e.quantity, e.price, order.side, order.time))
                        break
                elif e.price < order.price and order.quantity>0:
                    self.insert_limit_order(order)
            elif order.type==OrderType.MARKET:
                if e.quantity>order.quantity:
                    e.quantity-=order.quantity
                    filled_orders.append(FilledOrder(order.id, order.symbol, order.quantity, e.price, order.side, order.time))
                    filled_orders.append(FilledOrder(e.id, e.symbol, e.quantity, e.price, e.side, e.time))
                    order.quantity=0
                    break
                elif e.quantity<= order.quantity:
                    order.quantity -= e.quantity
                    filled_orders.append(FilledOrder(e.id, e.symbol, e.quantity, e.price, e.side, e.time))
                    removal.append(e)
                    if order.quantity == 0:
                        filled_orders.append(FilledOrder(order.id, order.symbol, e.quantity, e.price, order.side, order.time))
                        break
            elif order.type == OrderType.IOC:
                if e.quantity > order.quantity and e.price >= order.price:
                    e.quantity -= order.quantity
                    filled_orders.append(
                        FilledOrder(order.id, order.symbol, order.quantity, e.price, order.side, order.time))
                    filled_orders.append(FilledOrder(e.id, e.symbol, e.quantity, e.price, e.side, e.time))
                    break
                elif e.quantity <= order.quantity and e.price >= order.price:
                    order.quantity -= e.quantity
                    filled_orders.append(FilledOrder(e.id, e.symbol, e.quantity, e.price, e.side, e.time))
                    removal.append(e)
                    if order.quantity == 0:
                        filled_orders.append(FilledOrder(order.id, order.symbol, e.quantity, e.price, order.side, order.time))
                        break
        for i in removal:
            self.bid_book.remove(i)
        if order.quantity>0 and order.type==OrderType.LIMIT:
            self.insert_limit_order(order)

        return filled_orders

    def handle_limit_order(self, order):
        if order.side==OrderSide.BUY:
            filled_orders=self.handle_buy(order)
        elif order.side==OrderSide.SELL:
            filled_orders=self.handle_sell(order)
        else:
            raise UndefinedOrderSide("Undefined Order Side!")
        return filled_orders

    def handle_market_order(self, order):
        if order.side==OrderSide.BUY:
            filled_orders=self.handle_buy(order)
        elif order.side==OrderSide.SELL:
            filled_orders=self.handle_sell(order)
        else:
            raise UndefinedOrderSide("Undefined Order Side!")
        return filled_orders

    def handle_ioc_order(self, order):
        if order.side==OrderSide.BUY:
            filled_orders=self.handle_buy(order)
        elif order.side==OrderSide.SELL:
            filled_orders=self.handle_sell(order)
        else:
            raise UndefinedOrderSide("Undefined Order Side!")
        return filled_orders

    '''COMPLETE'''

    def insert_limit_order(self, order):
        try:
            assert order.type == OrderType.LIMIT
            if order.side == OrderSide.BUY:
                self.bid_book.append(order)
            else:
                self.ask_book.append(order)
        except:
            raise UndefinedOrderSide("Undefined Order Side!")
            return False
        self.sort_order()
        return True

    '''COMPLETE'''

    def amend_quantity(self, id, quantity):
        order=None
        for i in self.ask_book:
            if i.id==id:
                order=i
        for i in self.bid_book:
            if i.id==id:
                order=i
        if order!=None:
            if quantity > order.quantity:
                raise NewQuantityNotSmaller("Amendment Must Reduce Quantity!")
            self.cancel_order(order.id)
            order.quantity=quantity
            self.insert_limit_order(order)
        return False

    '''COMPLETE'''

    def cancel_order(self, id):
        for i in self.ask_book:
            if i.id == id:
                self.ask_book.remove(i)
                return True
        for i in self.bid_book:
            if i.id == id:
                self.bid_book.remove(i)
                return True
        return False


#
#
# class TestOrderBook(unittest.TestCase):
#
#     def test_insert_limit_order(self):
#         matching_engine = MatchingEngine()
#         order = LimitOrder(1, "S", 10, 10, OrderSide.BUY, time.time())
#         matching_engine.insert_limit_order(order)
#
#         self.assertEqual(matching_engine.bid_book[0].quantity, 10)
#         self.assertEqual(matching_engine.bid_book[0].price, 10)
#
    def test_handle_limit_order(self):
        matching_engine = MatchingEngine()
        order = LimitOrder(1, "S", 10, 10, OrderSide.BUY, time.time())
        matching_engine.insert_limit_order(order)

        order_1 = LimitOrder(2, "S", 5, 10, OrderSide.BUY, time.time())
        order_2 = LimitOrder(3, "S", 10, 15, OrderSide.BUY, time.time())
        matching_engine.handle_limit_order(order_1)
        matching_engine.handle_limit_order(order_2)

        self.assertEqual(matching_engine.bid_book[0].price, 15)
        self.assertEqual(matching_engine.bid_book[1].quantity, 10)

        order_sell = LimitOrder(4, "S", 14, 8, OrderSide.SELL, time.time())
        filled_orders = matching_engine.handle_limit_order(order_sell)

        self.assertEqual(matching_engine.bid_book[0].quantity, 6)
        self.assertEqual(filled_orders[0].id, 3)
        self.assertEqual(filled_orders[0].price, 15)
        self.assertEqual(filled_orders[2].id, 1)
        self.assertEqual(filled_orders[2].price, 10)
#
    def test_handle_market_order(self):
        matching_engine = MatchingEngine()
        order_1 = LimitOrder(1, "S", 6, 10, OrderSide.BUY, time.time())
        order_2 = LimitOrder(2, "S", 5, 10, OrderSide.BUY, time.time())
        matching_engine.handle_limit_order(order_1)
        matching_engine.handle_limit_order(order_2)

        order = MarketOrder(5, "S", 5, OrderSide.SELL, time.time())
        filled_orders = matching_engine.handle_market_order(order)
        self.assertEqual(matching_engine.bid_book[0].quantity, 1)
        self.assertEqual(filled_orders[0].price, 10)
#
#     def test_handle_ioc_order(self):
#         matching_engine = MatchingEngine()
#         order_1 = LimitOrder(1, "S", 1, 10, OrderSide.BUY, time.time())
#         order_2 = LimitOrder(2, "S", 5, 10, OrderSide.BUY, time.time())
#         matching_engine.handle_limit_order(order_1)
#         matching_engine.handle_limit_order(order_2)
#
#         order = IOCOrder(6, "S", 5, 12, OrderSide.SELL, time.time())
#         filled_orders = matching_engine.handle_ioc_order(order)
#         self.assertEqual(matching_engine.bid_book[0].quantity, 1)
#         self.assertEqual(len(filled_orders), 0)
#
#     def test_amend_quantity(self):
#         matching_engine = MatchingEngine()
#         order_1 = LimitOrder(1, "S", 5, 10, OrderSide.BUY, time.time())
#         order_2 = LimitOrder(2, "S", 10, 15, OrderSide.BUY, time.time())
#         matching_engine.handle_limit_order(order_1)
#         matching_engine.handle_limit_order(order_2)
#         matching_engine.amend_quantity(2, 8)
#         self.assertEqual(matching_engine.bid_book[0].quantity, 8)
#
#     def test_cancel_order(self):
#         matching_engine = MatchingEngine()
#         order_1 = LimitOrder(1, "S", 5, 10, OrderSide.BUY, time.time())
#         order_2 = LimitOrder(2, "S", 10, 15, OrderSide.BUY, time.time())
#         matching_engine.handle_limit_order(order_1)
#         matching_engine.handle_limit_order(order_2)
#
#         matching_engine.cancel_order(1)
#         self.assertEqual(matching_engine.bid_book[0].id, 2)
#
#     # The unittests must start with "test", change the function name to something that makes sense
#     def test_1(self):
#         # implement this unittest and three more
#         matching_engine = MatchingEngine()
#         # test if there is anybug when there is no available offer on the market
#         order = MarketOrder(5, "S", 5, OrderSide.SELL, time.time())
#         filled_orders = matching_engine.handle_market_order(order)
#         self.assertEqual(len(matching_engine.bid_book), 0)
#         self.assertEqual(len(filled_orders), 0)
#
#     def test_2(self):
#         matching_engine = MatchingEngine()
#         order_1 = LimitOrder(1, "S", 6, 10, OrderSide.SELL, time.time())
#         order_2 = LimitOrder(2, "S", 5, 11, OrderSide.SELL, time.time())
#         matching_engine.handle_limit_order(order_1)
#         matching_engine.handle_limit_order(order_2)
#         order = MarketOrder(5, "S", 20, OrderSide.BUY, time.time())
#         filled_orders = matching_engine.handle_market_order(order)
#         self.assertEqual(len(matching_engine.bid_book), 0)
#         self.assertEqual(filled_orders[0].price, 10)
#         self.assertEqual(filled_orders[1].price, 11)
#
#     def test_3(self):
#         matching_engine = MatchingEngine()
#         order_1 = LimitOrder(1, "S", 6, 10, OrderSide.SELL, time.time())
#         order_2 = LimitOrder(2, "S", 5, 11, OrderSide.SELL, time.time())
#         matching_engine.handle_limit_order(order_1)
#         matching_engine.handle_limit_order(order_2)
#
#         order = LimitOrder(5, "S", 20, 15, OrderSide.BUY, time.time())
#         filled_orders = matching_engine.handle_market_order(order)
#         self.assertEqual(len(matching_engine.bid_book), 1)
#         self.assertEqual(filled_orders[0].price, 10)
#         self.assertEqual(filled_orders[1].price, 11)
#         self.assertEqual(matching_engine.bid_book[0].quantity, 9)
#
#     def test_4(self):
#         matching_engine = MatchingEngine()
#         order_1 = LimitOrder(1, "S", 6, 10, OrderSide.SELL, time.time())
#         order_2 = LimitOrder(2, "S", 5, 11, OrderSide.SELL, time.time())
#         matching_engine.handle_limit_order(order_1)
#         matching_engine.handle_limit_order(order_2)
#
#         order = IOCOrder(5, "S", 20, 15, OrderSide.BUY, time.time())
#         filled_orders = matching_engine.handle_market_order(order)
#         self.assertEqual(len(matching_engine.bid_book), 0)
#
#         self.assertEqual(filled_orders[0].price, 10)
#         self.assertEqual(filled_orders[1].price, 11)
#
# if __name__=='__main__':
#     tester=TestOrderBook()
#     tester.test_1()
#     tester.test_2()
#     tester.test_3()
#     tester.test_4()