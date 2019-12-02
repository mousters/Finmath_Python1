import threading
import time
import random
class Trader(threading.Thread):
    def __init__(self,name,exchange,lock):
        #because this class is inherited from threading-->super
        super().__init__()
        self.name = name
        self.exchange=exchange
        self.lock=lock
    #run the in the thread (this method is overwritten, threading has a method called run)
    def run(self):
        while True:
            time.sleep(1)
            price_order=random.randrange(1,5)
            print('%s place an order for %d'
                        % (self.name,price_order))
            self.lock.acquire()
            self.exchange.handle_new_price({'name':self.name,\
                                            'price':price_order})
            self.lock.release()
class Exchange:
    def __init__(self):
        self.orders = {}
    def handle_new_price(self, neworder):
        #needs to copy-->bc data structure change outside can affect the code here
        o=neworder.copy()
        self.match(o['price'])
        self.orders[o['name']]=o['price']
    def match(self,n):
        for k,v in self.orders.items():
            if v==n:
                print("match between %s for %d " \
                      % (k,v))
if __name__=='__main__':
    exchange=Exchange()
    ex_lock = threading.Lock()
    trader1=Trader('Seb',exchange,ex_lock);trader2=Trader('Nic',exchange,ex_lock)
    trader2.start(); trader1.start()
    trader1.join(); trader2.join()
