from datetime import date

class Customer:
    def __init__(self, first_name:str, last_name:str, pesel:str, address:str, birth_date:str):
        self.first_name = first_name
        self.last_name = last_name
        self.pesel = pesel
        self.address = address
        self.birth_date = date.fromisoformat(birth_date)
        self.promotion_applied = False

    def __str__(self):
        return f'Customer("{self.first_name}", "{self.last_name}", "{self.pesel}", "{self.address}", "{self.birth_date.isoformat()}", "{self.promotion_applied}")'

    # Sets promotion_applied to True if customer's age is in <18,26> range 
    def apply_promotion(self):
        today = date.today()
        age = today.year - self.birth_date.year # year difference between today's date and customer birth_date
        if ((today.month, today.day) < (self.birth_date.month, self.birth_date.day)):
            age -= 1 # subtract one if customer doesn't have birthday in current year
        # print("age:", age)
        self.promotion_applied = 18 <= age <= 26
