class Coffee:
    def __init__(self, name):
        self.name = name

    def _get_name(self):
        return self._name
    def _set_name(self, name):
        if isinstance(name, str) and len(name) >= 3 and not hasattr(self, 'name'):
            self._name = name
        else:
            raise Exception("Coffee name must be a string and greater than or equal to 3 characters in length")
    name = property(_get_name, _set_name)
        
    def orders(self):
        return ([order for order in Order.all if order.coffee == self])
    
    def customers(self):
        customer_list = []
        for order in self.orders():
            if order.customer not in customer_list:
                customer_list.append(order.customer)
        return customer_list
    
    def num_orders(self):
        return len(self.orders())
    
    def average_price(self):
        total = 0.0
        for order in self.orders():
            total += order.price
        return total / self.num_orders()

class Customer:
    def __init__(self, name):
        self.name = name

    def _get_name(self):
        return self._name
    def _set_name(self, name):
        if isinstance(name, str) and len(name) >= 1 and len(name) <= 15:
            self._name = name
        else:
            raise Exception("Customer name must be a string and between 1 and 15 characters in length")
    name = property(_get_name, _set_name)
        
    def orders(self):
        return ([order for order in Order.all if order.customer == self])
    
    def coffees(self):
        coffee_list = []
        for order in self.orders():
            if order.coffee not in coffee_list:
                coffee_list.append(order.coffee)
        return coffee_list
    
    def create_order(self, coffee, price):
        if isinstance(coffee, Coffee):
            if isinstance(price, float):
                return Order(self, coffee, price)
            else:
                raise Exception("price must be a float")
        else:
            raise Exception("Coffee must be of type Coffee")
    
class Order:

    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all.append(self)

    def _get_price(self):
        return self._price
    def _set_price(self, price):
        if isinstance(price, float) and price > 1.0 and price < 10.0 and not hasattr(self, 'price'):
            self._price = price
        else:
            raise Exception("Price must be a float and between 0 and 10")
    price = property(_get_price, _set_price)

    def __get_customer(self):
        return self._customer
    def __set_customer(self, customer):
        if isinstance(customer, Customer):
            self._customer = customer
        else:
            raise Exception("Customer must be of type Customer")
    customer = property(__get_customer, __set_customer)

    def __get_coffe(self):
        return self._coffee
    def __set_coffee(self, coffee):
        if isinstance(coffee, Coffee):
            self._coffee = coffee
        else:
            raise Exception("Coffee must be of type Coffee")