
class order:
    def __init__(self, order_id, productname, price):  #-----consturctor------#
        self.order_id = order_id  #----instance variable----#
        self.productname = productname #-----instance variable----#
        self.price = price #-----instance variable----#

    def display_order(self):
        print(f"Order ID: {self.order_id}, Product: {self.productname}, Quantity: {self.price}")

    def add_discount(self):
        self.discount = 50 #--here we are creating instance variable inside method--#
    @classmethod
    def class_avail(cls,self):
        self.avail = True #--it will give error because avail is not instance variable--#

    
o1= order(10,"mp1",30)
o2= order(12,"mp2",40)
o3= order(11,"mp3",45)


o1.add_discount()
o2.add_discount()
o3.add_discount()

print(o1.__dict__) 
print(o2.__dict__) 
print(o3.__dict__) 



