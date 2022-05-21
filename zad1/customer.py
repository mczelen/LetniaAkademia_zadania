from datetime import date

class Customer:
    def __init__(self, first_name:str, last_name:str, pesel:str, birth_date:str):
        self.first_name = first_name
        self.last_name = last_name
        self.pesel = pesel
        self.birth_date = date.fromisoformat(birth_date)
        self.promotion_covered = False

    def __str__(self):
        return f'Customer("{self.first_name}", "{self.last_name}", "{self.pesel}", "{self.birth_date.isoformat()}")'