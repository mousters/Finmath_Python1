from collections import deque
import time
import random
from abc import ABC
# from  Matching_Engine import MatchingEngine
from enum import Enum
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

trader_to_exchange = deque()
exchange_to_trader = [deque() for _ in range(100)]


class MyThread:
    list_of_threads = []

    def __init__(self, id='NoID'):
        MyThread.list_of_threads.append(self)
        self.is_started = False
        self.id = id

    def start(self):
        self.is_started = True

    def join(self):
        pass
        # print('Trader ' + str(self.id) + ' will be waited')


# Each trader can take a separate action chosen from the list below:

# Actions:
# 1 - Place New Order/Order Filled
# 2 - Amend Quantity Of An Existing Order
# 3 - Cancel An Existing Order
# 4 - Return Balance And Position

# request - (Action #, Trader ID, Additional Arguments)

# result - (Action #, Action Return)

# WE ASSUME 'AAPL' IS THE ONLY TRADED STOCK.

import random
class Trader(MyThread):
    def __init__(self, id):
        super().__init__(id)
        self.book_position = 0
        self.balance_track = [1000000]
        # the traders each start with a balance of 1,000,000 and nothing on the books
        # each trader is a thread

    def place_limit_order(self, quantity=None, price=None, side=None):
        # Make sure the limit order given has the parameters necessary to construct the order
        # It's your choice how to implement the orders that do not have enough information
        # The 'order' returned must be of type LimitOrder
        # Make sure you modify the book position after the trade
        # You must return a tuple of the following:
        # (the action type enum, the id of the trader, and the order to be executed)
        order=LimitOrder(self.id,'APPL',quantity,price,side,time.time())
        request=(1, self.id, order)
        return request
    def place_market_order(self, quantity=None, side=None):
        order = MarketOrder(self.id, 'APPL', quantity, side, time.time())
        request=(1, self.id, order)
        return request
    def place_ioc_order(self, quantity=None, price=None, side=None):
        order = IOCOrder(self.id, 'APPL',  quantity, price,side, time.time())
        request=(1,self.id,order)
        return request
    def amend_quantity(self, quantity=None):
        # It's your choice how to implement the 'Amend' action where quantity is not given
        request=(2,self.id,quantity)
        # trader_to_exchange(order)
        # You must return a tuple of the following:
        # (the action type enum, the id of the trader, and quantity to change the order by)
        return request
    def cancel_order(self):
        # You must return a tuple of the following:
        # (the action type enum, the id of the trader)
        return (3,self.id)
    def balance_and_position(self):
        # You must return a tuple of the following:
        # (the action type enum, the id of the trader)
        return (4,self.id)

    def process_response(self, response):
        # Implement this function
        # You need to process each order according to the type (by enum) given by the 'response' variable
        if response[0][0] not in (1,2,3,4):
        # If the action taken by the trader is ambiguous you need to raise the following error
            raise UndefinedResponse("Undefined Response Received!")
        check = lambda x: 1 if (x ==OrderSide.SELL) else -1
        if response[0][0]==1 and response[0][2]!=None:
            for i in response[0][2]:
                if i.id!=self.id:
                    self.book_position+=check(i.side)*i.quantity
                    print('original balance',self.balance_track)
                    self.balance_track[0]-=check(i.side)*i.quantity*i.price
                    print('new balance', self.balance_track)

        if self.balance_track[0]==0:
            self.is_started=False


    def random_action(self):
        # Implement this function
        # According to the status of whether you have a position on the book and the action chosen
        # the trader needs to be able to take a separate action
        # The action taken can be random or deterministic, your choice
        action=random.randint(1,2)
        request=None
        if action==1:
            request=self.place_limit_order(int(self.balance_track[0]/ 2000),2000,OrderSide.BUY)
        elif action == 2:
            request = self.place_limit_order(int(self.balance_track[0]/ 2000),2000,OrderSide.SELL)
        return request

    def run_infinite_loop(self):
        # The trader needs to continue to take actions until the book balance falls to 0
        # While the trader can take actions, it chooses from a random_action and uploads the action
        # to the exchange
        #first process all the response
        temp_dq=exchange_to_trader[self.id]
        while len(temp_dq)>0:
            temp_response=temp_dq.pop()
            self.process_response(temp_response)

        if self.is_started:
            request=self.random_action()
            trader_to_exchange.appendleft(request)
        # The trader then takes any received responses from the exchange and processes it


class Exchange(MyThread):
    def __init__(self):
        super().__init__()
        self.balance = [1000000 for _ in range(10)]
        self.position = [0 for _ in range(10)]
        self.matching_engine = MatchingEngine()
        # The exchange keeps track of the traders' balances
        # The exchange uses the matching engine you built previously

    def place_new_order(self, order):
        # The exchange must use the matching engine to handle orders given
        results = []

        # The list of results is expected to contain a tuple of the follow form:
        # (Trader id that processed the order, (action type enum, order))
        filled_order = self.matching_engine.handle_order(order)
        results.append((1, order.id, filled_order))
        # The exchange must update the balance of positions of each trader involved in the trade (if any)
        check = lambda x: 1 if (x ==OrderSide.BUY) else -1
        if filled_order != None:
            for i in filled_order:
                if i.id !=order.id:
                    exchange.position[i.id] += check(i.side) * i.quantity
                    exchange.balance[i.id] -= check(i.side) * i.price * i.quantity

        return results

    def amend_quantity(self, id, quantity):
        # The matching engine must be able to process the 'amend' action based on the given parameters
        try:
            self.matching_engine.amend_quantity(id,quantity)
        except:
            raise NewQuantityNotSmaller("Amendment Must Reduce Quantity!")
            return (2,False)
        # Keep in mind of any exceptions that may be thrown by the matching engine while handling orders
        # The return must be in the form (action type enum, logical based on if order processed)
        return (2,True)

    def cancel_order(self, id):
        # The matching engine must be able to process the 'cancel' action based on the given parameters
        self.matching_engine.ca那ncel_order(id)
        return (3,True)
        # Keep in mind of any exceptions that may be thrown by the matching engine while handling orders
        # The return must be in the form (action type enum, logical based on if order processed)

    def balance_and_position(self, id):
        # The matching engine must be able to process the 'balance' action based on the given parameters

        # The return must be in the form (action type enum, (trader balance, trader positions))
        return (4,(self.balance[id],self.position[id]))

    def handle_request(self, request):
        # The exchange must be able to process different types of requests based on the action
        # type given using the functions implemented above

        if request[0]==1:
            response=self.place_new_order(request[2])
        elif request[0]==2:
            response=self.amend_quantity(request[1],request[2])
        elif request[0]==3:
            response =self.cancel_order(request[1])
        elif request[0]==4:
            response =self.balance[request[1]]
        else:
            raise UndefinedTraderAction("Undefined Trader Action!")
        return response
    def run_infinite_loop(self):
        # The exchange must continue handling orders as orders are issued by the traders
        # A way to do this is check if there are any orders waiting to be processed in the deque

        # If there are, handle the request using the functions built above and using the
        # corresponding trader's deque, return an acknowledgement based on the response
        while len(trader_to_exchange)>0:
            request=trader_to_exchange.pop()
            response=self.handle_request(request)
            if response[0][0]==1:
                exchange_to_trader[response[0][1]].appendleft(response)


if __name__ == "__main__":
    trader_to_exchange = deque()
    exchange_to_trader = [deque() for _ in range(10)]
    MyThread.list_of_threads=[]
    trader = [Trader(i) for i in range(10)]
    exchange = Exchange()

    exchange.start()
    for t in trader:
        t.start()

    exchange.join()
    for t in trader:
        t.join()

    sum_exch = 0
    for t in MyThread.list_of_threads:
        if t.id == "NoID":
            for b in t.balance:
                sum_exch += b

    print("Total Money Amount for All Traders before Trading Session: " + str(sum_exch))

    for i in range(2):
        # print(i,len(trader_to_exchange),len(exchange_to_trader))
        thread_active = False
        for t in MyThread.list_of_threads:
            print(t.is_started)
            if t.is_started:
                t.run_infinite_loop()
                thread_active = True

        if not thread_active:
            break

    sum_exch = 0
    for t in MyThread.list_of_threads:
        if t.id == "NoID":
            for b in t.balance:
                sum_exch += b

    print("Total Money Amount for All Traders after Trading Session: ", str(int(sum_exch)))
