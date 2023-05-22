class Customer:
    
    all = []
    
    def __init__(self, name):
        self.name = name
        Customer.all.append(self)
        self._coffees = []
        self._orders = []
        
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <=15:
            self._name = value
        else:
            raise Exception("Names must be between 1 and 15 characters, inclusive and be a string")
        
    def orders(self, new_order=None):
        from classes.order import Order
        all_orders = [order for order in Order.all if order.customer == self]
        if new_order and new_order not in all_orders:
            all_orders.append(new_order)
        return all_orders
        
    
    def coffees(self, new_coffee=None):
        from classes.coffee import Coffee
        return list(set([order.coffee for order in self.orders()]))