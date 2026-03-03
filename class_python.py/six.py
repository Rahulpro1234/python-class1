
class order:
    def __init__(self, order_id, productname, price):  #-----consturctor------#
        self.order_id = order_id  #----instance variable----#
        self.productname = productname #-----instance variable----#
        self.price = price #-----instance variable----#

o2= order(12,"mp2",40)

del o2.price
print(o2.__dict__)

