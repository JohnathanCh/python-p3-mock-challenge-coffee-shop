#!/usr/bin/env python3
import ipdb

from classes.customer import Customer
from classes.order import Order
from classes.coffee import Coffee

if __name__ == '__main__':
    print("HELLO! :) let's debug")
    
    customer1 = Customer("John")
    customer2 = Customer("Cole")
    coffee1 = Coffee("Mocha")
    coffee2 = Coffee("Black")
    coffee3 = Coffee("Frap-Crap")
    order1 = Order(customer1, coffee1, 5)
    order2 = Order(customer2, coffee2, 3)
    order3 = Order(customer1, coffee2, 7)
    order4 = Order(customer1, coffee3, 8)
    # order
    ipdb.set_trace()
