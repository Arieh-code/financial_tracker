from collections import defaultdict
from src.expense import Expense
from src.database import *
import datetime

class Budget:
    
    def __init__(self, user_id):
        self.user_id = user_id
        self.limits = defaultdict(float)  # category -> limit
        self.expenses = None # Use None to track if expenses have been loaded 
        
        self.load_limits()
        
    
    
    def load_limits(self):
        """Loads limits from db"""
        limits = get_limits_by_user(self.user_id)
        for limit in limits:
            self.limits[limit["category"]] = limit["amount"]
    
    
    def load_expenses(self, month: int = None):
        """Load expenses from DB on demand and cache them"""
        if self.expenses is None or month:
            expense_data = get_expenses_by_user(self.user_id)
            filtered_expense = [
                Expense.from_dict(data) for data in expense_data
                if not month or data["date"].month == month
            ]
            self.expenses = filtered_expense
       
    
    def set_limit(self, category: str, amount: float):
        """Sets a spending limit for a specific category."""
        if amount < 0:
            raise ValueError("Limit cannot be negative")
        set_limit(self.user_id, category, amount)
        self.limits[category] = amount
    
    
    
    def add_expense(self, expense: Expense):
        """Adds an expense and updates monthly and category totals."""
        insert_expense(expense.to_dict())
        if self.expenses is not None:
            self.expenses.append(expense)

        
            
    def check_limits(self):
        """Checks if spending in any category has approached or exceeded its limit.""" 
        current_month = datetime.date.today().month
        self.load_expenses(month=current_month)
        warnings = []
        category_total = defaultdict(float)
        for expense in self.expenses:
            category_total[expense.category] += expense.amount
        
        
        for category, limit in self.limits.items():
            if category_total[category] > limit:
                warnings.append(f"Warning: Spending for {category} exceeded its limit")
            elif category_total[category] >= 0.9 * limit:
                warnings.append(f"Warning: Spending for {category} is approaching its limit")
        
        return warnings
    
    
  
    
    def get_expenses(self, **kwargs) -> float:
            
        """Calculates total expenses with optional filters for category and month.
        
        Args:
            month (int, optional): Month to filter expenses by.
            category (str, optional): Category to filter expenses by.
        
        Returns:
            float: The total expenses based on specified filters.
        """
        month = kwargs.get("month")
        category = kwargs.get("category")
        query = {"user_id": self.user_id}

        # Filter by month if specified
        if month is not None:
            current_year = datetime.datetime.now().year
            start_date = datetime.datetime(current_year, month, 1)
            # Calculate the end date as the first day of the next month
            end_date = datetime.datetime(current_year, month % 12 + 1, 1)
            query["date"] = {"$gte": start_date, "$lt": end_date}

        # Filter by category if specified
        if category is not None:
            query["category"] = category

        # Query MongoDB with filters and calculate the total
        expenses = db["expenses"].find(query)
        total = sum(expense["amount"] for expense in expenses)
        
        return total