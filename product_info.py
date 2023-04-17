from abc import ABC, abstractmethod
from typing import List
from interactive_entities import Person, Vendor, Customer

class review:
    def init(self, review_id: int, customer: Customer, product: str, rating: int, comments: str):
        self.review_id = review_id
        self.customer = customer
        self.product = product
        self.rating = rating
        self.comments = comments

    def review_id_validity(self, review_id):
        if (review_id > 10000) or (review_id < 100):
            return 0
        else: 
            return 1

    def cheating_test(self, rating, review_id):
        cheating_score = (rating > 80) * (rating / 100)
        return cheating_score
    
class product:
    _default_discount = 7 #percent
    all_products = []

    def init(self, product_id: int, name: str, price: float, available: bool, category: str, quantity: int):
        self.__product_id = product_id
        self.name = name
        self.price = price
        self.category = category
        self.available = available
        self.discount = product._default_discount
        self.quantity = quantity
        product.all_products.append(self)

    def get_price(self) -> float:
        final_price = self.price * (1 - self.discount / 100)
        return final_price
    
    def total_revenue(self, quantity, get_price):
        total_revenue = quantity * get_price
        return total_revenue
    
    def __update(self) -> None:
        for index in range(len(product.all_products)):
            if product.all_products[index].__product_id == self.__product_id:
                product.all_products[index] = self
                break


    def description(self) -> None:
        print(f"This product's id is {self._product_id}.")
        print(f"name of the product is {self.name}.")
        print(f"the price of this product is {self.price}.")
        print(f"the category of this product {self.category}.")
        print(f"You can buy this product only with: {self.get_price()}$")

class category:
    def init(self, category_id: int, name: str, description: str, products: List["product"], parent_category: str):
        self.category_id = category_id
        self.name = name
        self.description = description
        self.products = products
        self.parent_category = parent_category

    def intrest_rate(self) -> None:
        if self.category_id > 10000:
            print("This category is sky rocketing !")
        else:
            print("Nothing much going on in this category")

class inventory:
    def init(self, inventory_id: int, quantities: int, store: str, products: List["product"], capacity: int, expantion_price: int):
        self.inventory_id = inventory_id
        self.quantities = quantities
        self.store = store
        self.products = products
        self._capacity = capacity

    def is_full(self, capacity, quantities) -> bool:
        if capacity > quantities:
            return 1
        else:
            return 0
        
    def expand_possibility(self, capacity, expantion_price) -> bool:
        total_revenue = product.total_revenue
        if total_revenue > expantion_price:
            return 1
        else:
            return 0
        
class item:
    def init(self, item_id: int, product: product, quantity: int, price: float, total_price: float):
        self.item_id = item_id
        self.product = product
        self.quantity = quantity
        self.__price = price
        self._total_price = total_price

    def get_discount(self, quantity, price, total_price) -> int:
        calculated_revenue = quantity * price
        discount = 1 - total_price / calculated_revenue
        return discount
    
class shopping_cart:
    _default_average_price = 150

    def init(self, cart_id: int, customer: Customer, items: List[item], total: float, date_created: int, average_price: int):
        self.cart_id = cart_id
        self.__customer = customer
        self.items = items
        self._total = total
        self.date_created = date_created
        self.average_price = average_price

    def affortibality(self, average_price) -> bool:
        if average_price > shopping_cart.default_average_price:
            return 0
        else:
            return 1
        
class order:
    _default_speed = 1
    _average_expected_date = 65

    def init(self, order_id: int, customer: Customer, items: List[item], total: float, date: int):
        self.order_id = order_id
        self.__customer = customer
        self.items = items
        self._total = total
        self.date = date

    def emergency_delivery(self, date) -> int:
        while date > order._average_expected_date:
            order._default_speed += 1
            date -= 1
        return date
