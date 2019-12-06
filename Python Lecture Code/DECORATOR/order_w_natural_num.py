def type_checker(n,list):
    check=1
    if isinstance(n,Order):
        list.append(n.quantity)
    else:
        if type(n) != int or n < 0:
            check = 0
        else:
            list.append(n)
    return check,list
def argument_test_natural_number(f):
    def helper(x,y,z):
        value=[]
        check, value = type_checker(x,value)
        check, value = type_checker(y, value)
        check, value = type_checker(z, value)
        if(check==1):
            return sum(value)
        else:
            print('Error Reached')
            raise Exception ("Argument is not an integer")
    return helper

class Order:
    # you should leave the constructor unchanged
    def __init__(self, a, b):
        self.price = a
        self.quantity = b
    # Slide 14
    @property
    def price(self):
        return self.__price
    @property
    def quantity(self):
        return self.__quantity
    # when you create the setter, you need to check if quantity >=0
    @quantity.setter
    def quantity(self, val):
        if (val < 0):
            self.__quantity = 0
        else:
            self.__quantity = val

    @price.setter
    def price(self, val):
        if (val < 0):
            self.__price = 0
        else:
            self.__price = val

    @staticmethod
    @argument_test_natural_number
    def add_quantity_for_two_orders_and_one_number(a, b, c):
        return a.quantity + b.quantity + c

    def __repr__(self):
        return 'The order has quantity: {0} and price {1} '.format(self.quantity,self.price)
if __name__=='__main__':
    x=Order(10,100);x.quantity=15;x.price=15
    print(x)
    # The order has quantity: (15, 15) and price(15, 15)

    y=Order(10,100);y.quantity=13;y.price=16
    print(y)
    # The order has quantity: (13, 16) and price(13, 16)

    y.quantity=-100
    print(Order.add_quantity_for_two_orders_and_one_number(100,y,100))
    #because when quantity = - 100, the decorator set the quantity as 0 line 46
    # 200
    print(y)
    # The order has quantity: 0 and price 16

