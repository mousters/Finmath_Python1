import ast
import numpy as np
import pickle
import json
order = { "type" : " FOK", "side" : "buy"}
repr(order)
with open('simple_writing.txt','w') as f:f.write(repr(order))
with open('simple_writing.txt','r') as f: inp=ast.literal_eval(f.read())
print(inp)

#BYTE REPRESENTATION
orders = { 'side ': ' buy', 'price': 72 , 'quantity': 87}
byte_out=pickle.dumps(orders)
print(byte_out)
print(type(byte_out))
# b'\x80\x03}q\x00(X\x05\x00\x00\x00side q\x01X\x04\x00\x00\x00 buyq\x02X\x05\x00\x00\x00priceq\x03KHX\x08\x00\x00\x00quantityq\x04KWu.'
received_in=pickle.loads(byte_out)
print(received_in)
#{'side ': ' buy', 'price': 72, 'quantity': 87}
#the encoding part makes the output bytes
byte_out2=json.dumps(order).encode('utf-8')
print(byte_out2)
