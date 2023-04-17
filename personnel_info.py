from customer_info import Address


class store:
    def init(self, store_id: int, name: str, promo_id: int, adderess: Address, phone_number: str, email: str, website: str):
        self.store_id = store_id
        self.name = name
        self.__promo_id = promo_id
        self.adderess = adderess
        self._phone_number = phone_number
        self.__email = email
        self.website = website

    def email_validation(self, email) -> bool:
        if (len(email) > 10) & ("@" in email):
            return 1
        else:
            return 0
        
class promotion:
    def init(self, promo_id: int, name: str, discount: float, start_date: str, end_date: str, days_off: int):
        self.__promo_id = promo_id
        self.name = name
        self._discount = discount
        self.start_date = start_date
        self.end_date = end_date
        self.days_off = days_off

    def work_record(self, start_date, end_date) -> int:
        duration = end_date - start_date
        return duration
    
    def equal_oppertunities(self, days_off) -> bool:
        if (days_off <= 5) & (promotion.work_record() >= 240):
            return 1
        else:
            return 0