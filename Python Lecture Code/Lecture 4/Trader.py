import threading
import time
import random
class Trader(threading.Thread):
    def __init__(self,name):
        #because this class is inherited from threading-->super
        super().__init__()
        self.name = name
    #run the in the thread (this method is overwritten, threading has a method called run)
    def run(self):
        while True:
            time.sleep(1)
            price_order=random.randrange(1,5)
            print('%s place an order for %d'
                        % (self.name,price_order))
'''
    trader1=Trader('Seb');trader2=Trader('Nic')
    trader2.start(); trader1.start()
    trader1.join(); trader2.join()
'''
class Exchange:
    def __init__(self):
        self.orders = {}
    def handle_new_price(self, neworder):
        o=neworder.copy()
        self.match(o['price'])
        self.orders[o['name']]=o['price']
    def match(self,n):
        for o in self.orders:
            if o['price']==n:
                print("match between %s for %d " \
                      % (o['name'], o['price']))

