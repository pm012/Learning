from uuid import uuid1

class NotEnoughRights(Exception):
    def __init__(self, *value: object) -> None:
        self.value = value

    def __str__(self):
        return 'You have not enough rights for this' + repr(self.value)
    

class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Order:
    def __init__(self, id_=None):
        if id_ is None:
            id_ = uuid1().int
        self.id = id_
        self.items = list()
        self.total = 0

    def __add__(self, item):
        self.items.append(item)
        self.total += item.price

    def __sub__(self, item):
        if item in self.items:
            self.items.remove(item)
            self.total -= item.price

    def __str__(self):
        msg = f"Items\n"
        if self.items:
            for item in self.items:
                msg += f"{item.name}:{item.price}\n"

        msg += f"Total: {self.total}"

        return msg
    
class Person:
    def add(self, *args):
        raise NotEnoughRights
    
    def sub(self, *args):
        raise NotEnoughRights
    
    def view(self, *args):
        raise NotEnoughRights
    
    def check(self, *args):
        raise NotEnoughRights
    
    def confirm(self, *args):
        raise NotEnoughRights
    
    def complete(self, *args):
        raise NotEnoughRights
    

class Customer(Person):
    def view(self, order):
        return str(order)
    
class Seller(Person):
    def add(self, item, order = None):
        if order is None:
            order = Order()
        order + item
        return order
    
    def sub(self, item, order):
        order - item

    def confirm(self, order, manufacturer):
        manufacturer.add(order)


class Manufacturer(Person):
    def __init__(self):
        self.orders = dict()

    @property
    def order_list(self):
        return list(self.orders.keys())
    
    def add(self, order):
        self.orders[order.id] = False

    def view(self, order):
        if order.id in self.orders:
            return self.orders[order.id]
        
    def check(self, order):
        return self.orders[order.id]
    
    def complete(self, order):
        if order.id in self.orders:
            self.orders[order.id]=True
    



    def view(self, order):
        return str(order)
    

#TODO add checks

ball = Item("Ball", 10)
cup = Item("Cup", 5)
bag = Item("Bag", 15)

seller = Seller()
customer = Customer()
manufacturer = Manufacturer()

        

    
    
    
    


                