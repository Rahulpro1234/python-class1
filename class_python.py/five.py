
#update----------------
class order:
    def __init__(self, order_id, productname, price):  #-----consturctor------#
        self.order_id = order_id  #----instance variable----#
        self.productname = productname #-----instance variable----#
        self.price = price #-

o3= order(11,"mp3",45)

o3.price = 48
print(o3.__dict__)


