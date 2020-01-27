class FinancialProduct:
    def __init__(self,description,product_code, type):
        self.description=description
        #two underscore means private code
        self.__product_code=product_code
        self.type=type
    def change_description(self,description):
        self.description=description
    def get_product_code(self):
        return self.__product_code
    def __repr__(self):
        return self.description+" code: "+self.get_product_code()
class Stock(FinancialProduct):
    def __init__(self,description,product_code):
        super().__init__(description,product_code,'Stock')
    def __repr__(self):
        return super().__repr__()+' Type: Stock'
#class that behave like functions
import math
class gaussian:
    def __init__(self,exponent):
        self.exponent=exponent
    def __call__(self,p):
        return math.exp(-self.exponent*p*p)
if __name__=='__main__':
    line='I am going to split the line'
    print('line: ',line)
    print('called func : line.split()')
    print(line.split())
    #['I', 'am', 'going', 'to', 'split', 'the', 'line']
    #tuple is immutable t1=(1,2)
    #change tuple to mutable by list(t1)

    #initialize list
    my_list = [e for e in range(101)]
    #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, ...]

    #intialize dictionary
    cars=dict()
    cars['ford']=200
    cars['toyoto']=300
    print(cars)
    #{'ford': 200, 'toyoto': 300}
    for c,p in cars.items():
        print(c, p)
    #ford 200
    #toyoto 300

    #financial product testing
    fp1=FinancialProduct('Apple','APPL','Stock')
    print(fp1)
    #Apple code: APPL

    try:
        # this following code does not execute b/c product code is private
        fp1.product_code
    except:
        print(fp1.get_product_code())

    #stock testing
    st1=Stock('Apple','APPL')
    print(st1)
    #Apple code: APPL Type: Stock

    #function-like class
    gaus=gaussian(1)
    print('exp(-4) = ',gaus(2))
    #exp(-4) =  0.01831563888873418

import datetime
datetime.datetime.now().minute