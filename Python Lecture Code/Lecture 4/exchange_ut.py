import unittest

from Trader import Exchange
'''
class TestExchangeMethods(unittest.TestCase):
    def test_one_order(self):
        exch1=Exchange()
        o1={'name' : 'seb',
            'price' : 5}
        exch1.handle_new_price(o1)
        self.assertEqual(exch1.orders['seb'], 5)
    def test_2_orders(self):
        exch1=Exchange()
        o1={'name' : 'seb',
            'price' : 5}
        o2 = {'name': 'nic',
              'price': 4}
        exch1.handle_new_price(o1)
        self.assertEqual(exch1.orders['seb'], 5)
        exch1.handle_new_price(o2)
        self.assertEqual(exch1.orders['nic'], 4)
'''
