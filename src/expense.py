from datetime import datetime, date as date_type
from src.database import insert_expense
class Expense:
    
    def __init__(self, amount:float, category:str, description:str, user_id:str, date=None):
        self.amount = amount
        self.category = category
        # self.date = date if isinstance(date, datetime) else datetime.combine(date or datetime.now(), datetime.min.time())
        self.description = description
        self.user_id = user_id
        
        if date is None:
            self.date = datetime.now()  # Use current date and time if no date is provided
        elif isinstance(date, date_type):  # Check if it's a date (or datetime)
            # Convert date to datetime if necessary
            self.date = datetime.combine(date, datetime.min.time()) if isinstance(date, date_type) and not isinstance(date, datetime) else date
        else:
            raise ValueError("Date must be a datetime.date or datetime.datetime object")

        
        # make sure that the amount is positive
        if self.amount < 0:
            raise ValueError("Amount cannot be negative")        
        
    def __str__(self):
        return f"| {self.date} - {self.user_id} | {self.description} | ${self.amount:.2f} | {self.category} |" 
    
    
    def to_dict(self):
        """ Convert Expense into json format for mongoDB usage"""
        
        return {
            "amount": self.amount,
            "category": self.category,
            "description": self.description,
            "user_id": self.user_id,
            "date": self.date
        }
        
    
    @classmethod
    def from_dict(cls, data):
        """ Create an Expense object from data in mongoDB"""
        return cls(
            amount = data["amount"],
            category = data["category"],
            description = data["description"],
            user_id = data["user_id"],
            date = data["date"]
        )    
        
    def save(self):
        insert_expense(self.to_dict())