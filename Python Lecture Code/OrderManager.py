class OrderManager:
    def __init__(self):
        self.orders=[]

    def handle_order_from_strategy(self,order):
        self.orders.append(order)

    def get_volume(self):
        sum_quantity = 0
        for o in self.orders:
            sum_quantity+=o['quantity']
        return sum_quantity

    def get_total_of_non_acked_orders(self):
        nb_orders = 0
        for o in self.orders:
            if o['state']=='New':
                nb_orders+=1
        return nb_orders

    def handle_execution_report(self, execution_report):
        for o in self.orders:
            if o['id']==execution_report['id']:
                o['state']=execution_report['state']
                return
        print('Order not found')

    #unit test revisit
    #https://piazza.com/class/k077xovqaeh3pq?cid=9