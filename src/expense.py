import datetime
class Expense:
    
    def __init__(self, amount:float, category:str, date:datetime.date, description:str):
        self.amount = amount
        self.category = category
        self.date = date
        self.description = description
        
        # make sure that the date instance is of type datetime
        if not isinstance(self.date, datetime.date):
            raise ValueError("Date must be a datetime.date object")
        
        # make sure that the amount is positive
        if self.amount < 0:
            raise ValueError("Amount cannot be negative")        
    
    def __str__(self):
        return f"{self.description} | ${self.amount:.2f} | {self.date} | {self.category}" 
    