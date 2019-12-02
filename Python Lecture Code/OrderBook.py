class OrderBook:
    # CONSTRUCTOR !!!!!!!!!
    def __init__(self, symbol):
        self.bids = []
        self.offers = []

    def add_order(self, order):
        if order['side']=='bid':
            self.bids.append(order)
        elif order['side']=='offer':
            self.offers.append(order)
        else:
            print('stupid !!!')
        self.bids.sort(key=lambda x:x['price'],reverse=True)
        self.offers.sort(key=lambda x: x['price'],reverse=False)
    def amend_order(self):
        pass
    def cancel_order(self):
        pass
    def get_top_of_book(self):
        return (self.bids[0],self.offers[0])
if __name__ =='__main__':
    order1={'price' : 10, 'quantity' : 100, 'symbol' : 'AAPL', 'side' : 'bid'}
    ob1=OrderBook('AAPL')
    ob1.add_order(order1.copy())
    order1['price']=11
    ob1.add_order(order1.copy())
    order1['price']=9
    ob1.add_order(order1.copy())
    print(ob1.bids)