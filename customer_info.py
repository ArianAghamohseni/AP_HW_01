from typing import List

class ContactInfo:
    def init(self, phone_number: str, email: str, social_media_handles: List[str],
                 mailing_address: 'Address', is_active: bool):
        self.phone_number = phone_number
        self.email = email
        self.social_media_handles = social_media_handles
        self.mailing_address = mailing_address
        self.is_active = is_active

    def _update_phone_number(self, new_number: str) -> None:
        self.phone_number = new_number

    def _update_email(self, new_email: str) -> None:
        self.email = new_email


class Address:
    def init(self, street: str, city: str, state: str, zip_code: str, country: str):
        self.street = street
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.country = country

    def __get_full_address(self) -> str:
        return f"{self.street}, {self.city}, {self.state} {self.zip_code}, {self.country}"
    
class PaymentInfo:
    def init(self, payment_id: int, card_number: str, expiration_date: str, security_code: str, billing_address: Address):
        self.payment_id = payment_id
        self.card_number = card_number
        self.expiration_date = expiration_date
        self.security_code = security_code
        self.billing_address = billing_address
    
    def update_card_info(self, field: str, value: str):
        if hasattr(self, field):
            setattr(self, field, value)
            
    def __add_billing_address(self, address):
        self.billing_address = address