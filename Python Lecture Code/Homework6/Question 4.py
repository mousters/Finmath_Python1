import json

class Order:
    def __init__(self,price,quantity,side):
        self.price=price
        self.quantity=quantity
        self.side=side

class OrderEncoder(json.JSONEncoder):
    def default(self,z):
        if isinstance(z,Order):
            result=dict()
            result["price"]=z.price
            result['quantity']=z.quantity
            result['side']=z.side
            return result
        else:
            return None
o1 = Order(12,100,"buy")
o2 = Order(22,50,"sell")

encod1=json.dumps(o1, cls=OrderEncoder)
print(encod1)
print(type(encod1))
encod2=json.dumps(o2, cls=OrderEncoder)
print(encod1)
print(type(encod1))