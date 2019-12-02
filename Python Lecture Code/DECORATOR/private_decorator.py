class MyClass:
    def __init__(self, a):
        #WITH DECORATOR THIS ATTRIBUTE CAN BE SET TO PRIVATE
        self.__OurAtt = a
    @property
    def OurAtt(self):
        return self.__OurAtt
    #WITHOUT THIS PART, y.OurAtt CAN RETURN THE ATTRIBUTE BUT CANNOT MODIFY THE ATTR
    @OurAtt.setter
    def OurAtt(self, val):
        if val < 0:
            self.__OurAtt = 0
        elif val > 1000:
            self.__OurAtt = 1000
        else:
            self.__OurAtt = val

y = MyClass(10)
y.OurAtt=2
print(y.OurAtt)