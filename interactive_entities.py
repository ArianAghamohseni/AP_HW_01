from abc import ABC, abstractmethod
from typing import List


class Person(ABC):
    def init(self, name: str, age: int, gender: str, occupation: str, email: str):
        self.name = name
        self.age = age
        self.gender = gender
        self.occupation = occupation
        self.email = email

    @abstractmethod
    def get_info(self) -> str:
        pass

    def get_name(self) -> str:
        return self.name
    
    def set_name(self, name: str) -> None:
        self.name = name
    
    def get_age(self) -> int:
        return self.age
    
    def set_age(self, age: int) -> None:
        self.age = age
    
    def get_gender(self) -> str:
        return self.gender
    
    def set_gender(self, gender: str) -> None:
        self.gender = gender
    
    def get_occupation(self) -> str:
        return self.occupation
    
    def set_occupation(self, occupation: str) -> None:
        self.occupation = occupation
    
    def get_email(self) -> str:
        return self.email
    
    def set_email(self, email: str) -> None:
        self.email = email

    def update_email(self, new_email: str) -> None:
        self.email = new_email

    def send_email(self, message: str) -> None:
        print(f"Email sent to {self.name} ({self.email}): {message}")

    def get_age_group(self) -> str:
        if self.age < 18:
            return "Child"
        elif self.age < 60:
            return "Adult"
        else:
            return "Senior"


class Customer(Person):
    def init(self, name: str, age: int, gender: str, occupation: str, email: str,
                 account_id: int, contact_info: str, billing_address: str,
                 shipping_address: str, orders: List[set]):
        super().init(name, age, gender, occupation, email)
        self.account_id = account_id
        self.contact_info = contact_info
        self.billing_address = billing_address
        self.shipping_address = shipping_address
        self.orders = orders

    def get_info(self) -> str:
        return f"{self.name}, {self.get_age_group()}, Customer"

    def place_order(self, order: str) -> None:
        self.orders.append(order)

    def cancel_order(self, order_id: int) -> None:
        for order in self.orders:
            if order.order_id == order_id:
                order.cancel()
                self.orders.remove(order)
                break

    def view_order_history(self) -> List[str]:
        return self.orders


class Vendor(Person):
    def init(self, name: str, age: int, gender: str, occupation: str, email: str,
                 vendor_id: int, address: str, phone_number: str, products: List[str]):
        super().init(name, age, gender, occupation, email)
        self.vendor_id = vendor_id
        self.address = address
        self.phone_number = phone_number
        self.email = email
        self.products = products

    def get_info(self) -> str:
        return f"{self.name}, {self.get_age_group()}, Vendor"

    def add_product(self, product: str) -> None:
        self.products.append(product)

    def remove_product(self, product_id: int) -> None:
        for product in self.products:
            if product.product_id == product_id:
                self.products.remove(product)
                break

    def update_product_price(self, product_id: int, new_price: float) -> None:
        for product in self.products:
            if product.product_id == product_id:
                product.update_price(new_price)
                break