class OrderBook:
    def __init__(self):
        self.list_asks = []
        self.list_bids = []
        # the list of bids and offers is self explanatory.
        # the orders attribute keeps a record of all the orders where they key is the order id and the
        # value is the order. If used correctly, this should help you implement the handle methods below.
        self.orders = {}

    def handle_order(self, o):
        if o['action'] == 'new':
            self.handle_new(o)
        elif o['action'] == 'modify':
            self.handle_modify(o)
        elif o['action'] == 'delete':
            self.handle_delete(o)
        else:
            print('Error-Cannot handle this action')

    def handle_new(self, o):
        self.orders[o['id']] = o
        if o["side"] == 'bid':
            self.list_bids.append(o)
        else:
            self.list_asks.append(o)

        self.list_bids = sorted(self.list_bids, key=lambda o: o['price'], reverse=True)
        self.list_asks = sorted(self.list_asks, key=lambda o: o['price'])

    def handle_modify(self, o):
        for idx, order in enumerate(self.list_bids):
            if order['id'] == o['id']:
                self.list_bids[idx]['quantity'] = o['quantity']
        for idx, order in enumerate(self.list_asks):
            if order['id'] == o['id']:
                self.list_asks[idx]['quantity'] = o['quantity']

        self.list_bids = sorted(self.list_bids, key=lambda o: o['price'], reverse=True)
        self.list_asks = sorted(self.list_asks, key=lambda o: o['price'])

    def handle_delete(self, o):
        self.orders = {}
        for idx, order in enumerate(self.list_bids):
            if order['id'] == o['id']:
                self.list_bids.remove(order)
        for idx, order in enumerate(self.list_asks):
            if order['id'] == o['id']:
                self.list_asks.remove(order)

        self.list_bids = sorted(self.list_bids, key=lambda o: o['price'], reverse=True)
        self.list_asks = sorted(self.list_asks, key=lambda o: o['price'])

    def find_order_in_a_list(self, o, lookup_list=None):
        pass

    def display_content(self, fptr):
        # you certainly don't need to touch this part
        fptr.write('BIDS\n')
        for o in self.list_bids:
            fptr.write("%d %d %d\n" % (o['id'], o['price'], o['quantity']))
        fptr.write('OFFERS\n')
        for o in self.list_asks:
            fptr.write("%d %d %d\n" % (o['id'], o['price'], o['quantity']))