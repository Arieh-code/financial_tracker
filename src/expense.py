import datetime
from src.database import insert_expense
class Expense:
    
    def __init__(self, amount:float, category:str, description:str, user_id:str, date=None):
        self.amount = amount
        self.category = category
        self.date = date or datetime.date.today()
        self.description = description
        self.user_id = user_id
        
        # make sure that the date instance is of type datetime
        if not isinstance(self.date, datetime.date):
            raise ValueError("Date must be a datetime.date object")
        
        # make sure that the amount is positive
        if self.amount < 0:
            raise ValueError("Amount cannot be negative")        
    
    
    def save_to_db(self):
        """ convert the instance into a dictionary and save it to mongoDB """
        expense_data = {
            "amount": self.amount,
            "category": self.category,
            "date": self.date.isoformat(),
            "description": self.description,
            "user_id": self.user_id  # automatically set the created_at timestamp
        }
        
        insert_expense(expense_data)
        
    def __str__(self):
        return f"| {self.date} - {self.user_id} | {self.description} | ${self.amount:.2f} | {self.category} |" 
    