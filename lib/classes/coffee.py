from statistics import mean 
class Coffee:
    
    all = []
    
    def __init__(self, name):
        self.name = name
        self._customers = []
        self._orders = []
        Coffee.all.append(self)
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str) and not hasattr(self, 'name'):
            self._name = value
        else:
            raise Exception('Name of coffe can not be changed after the coffee is created')
        
    def orders(self, new_order=None):
        from classes.order import Order
        all_orders =  [order for order in Order.all if order.coffee == self]
        if new_order is not None and isinstance(new_order, Order) and new_order not in all_orders:
            all_orders.append(new_order) 
        return all_orders
    
    def customers(self, new_customer=None):
        from classes.customer import Customer
        return list(set([order.customer for order in self.orders()]))
    
    def num_orders(self):
        return len(self.orders())
    
    def average_price(self):
        prices = [order.price for order in self.orders()]
        return mean(prices)