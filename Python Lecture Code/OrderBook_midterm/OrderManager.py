class OrderManager:
    counter = 1

    def __init__(self):
        self.orders = []

    def handle_order_from_ts(self, o):
        orderid = OrderManager.counter
        OrderManager.counter += 1
        o["id"] = orderid
        o["state"] = "new"
        self.orders.append(o.copy())

    def handle_order_from_market(self, o):
        for order in self.orders:
            if o["id"] == order["id"]:
                order["state"] = o["state"]
                return
        print("order id {} not found".format(o["id"]))

    def get_positions(self):
        sum_quantity = 0
        for order in self.orders:
            if order["state"] == "filled" and order["side"] == "buy":
                sum_quantity += order["quantity"]
            if order["state"] == "filled" and order["side"] == "sell":
                sum_quantity -= order["quantity"]
        return sum_quantity

    def get_holdings(self):
        sum_holdings = 0
        for order in self.orders:
            if order["state"] == "filled" and i["side"] == "buy":
                sum_holdings += order["quantity"] * order["price"]
            if order["state"] == "filled" and order["side"] == "sell":
                sum_holdings -= order["quantity"] * order["price"]
        return sum_holdings

    def get_total_filled(self):
        filled_orders = 0
        for order in self.orders:
            if order["state"] == "filled":
                filled_orders += 1
        return filled_orders

    def get_unacknowledged_orders(self):
        unacked_orders = 0
        for order in self.orders:
            if order["state"] == "new":
                unacked_orders += 1
        return unacked_orders

    def get_unacknowledged_buy_volume(self):
        unacked_buy_volumne = 0
        for order in self.orders:
            if order["side"] == "buy":
                unacked_buy_volumne += order["quantity"] * order["price"]
        return unacked_buy_volumne

    def get_unacknowledged_sell_volume(self):
        unacked_buy_volumne = 0
        for order in self.orders:
            if order["side"] == "sell":
                unacked_buy_volumne += order["quantity"] * order["price"]
        return unacked_buy_volumne