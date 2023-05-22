
class Order:
    
    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        customer.orders(self)
        coffee.orders(self)
        Order.all.append(self)
        
        @property
        def customer(self):
            return self._customer
        
        @customer.setter 
        def customer(self, customer):
            from classes.customer import Customer
            if isinstance(customer, Customer):
                self._customer = customer
            else:
                raise TypeError("customer must be a Customer")
            
        @property
        def coffee(self):
            from classes.coffee import Coffee
            if isinstance(coffee, Coffee):
                self._coffee = coffee
            else:
                raise TypeError("coffee must be a Coffee")
