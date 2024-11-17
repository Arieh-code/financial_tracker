from collections import defaultdict
from src.expense import Expense
import datetime

class Budget:
    
    def __init__(self):
        self.limits = defaultdict(float)  # category -> limit
        self.expenses = defaultdict(list) # month -> Expenses list 
        self.monthly_expenses = defaultdict(lambda: defaultdict(float)) # month -> category -> expenses sum
        
    
    def set_limit(self, category: str, amount: float):
        """Sets a spending limit for a specific category."""
        if amount < 0:
            raise ValueError("Limit cannot be negative")
        else:
            self.limits[category] = amount
    
    
    
    def add_expense(self, expense: Expense):
        """Adds an expense and updates monthly and category totals."""
        month = expense.date.month 
        amount = expense.amount
        category = expense.category
        self.expenses[month].append(expense)
        self.monthly_expenses[month][category] += amount
        
            
    def check_limits(self):
        """Checks if spending in any category has approached or exceeded its limit.""" 
        warnings = []
        current_month = datetime.date.today().month
        
        for category, limit in self.limits.items():
            if self.monthly_expenses[current_month][category] > limit:
                warnings.append(f"Warning: Spending for {category} exceeded its limit")
            elif self.monthly_expenses[current_month][category] >= 0.9 * limit:
                warnings.append(f"Warning: Spending for {category} is approaching its limit")
        
        return warnings
    
    
    def get_monthly_summary(self, month: int=None):
        """Returns the total expenses per category for a given month."""
        month = month or datetime.date.today().month
        return self.monthly_expenses.get(month, {})
        
        
    # def get_total_expenses(self):
    #     """Calculates the total expenses across all categories and months."""
        
    #     total = sum(
    #         amount for month in self.monthly_expenses.values()
    #         for amount in month.values()
    #     )
        
        
    #     return total
    
    
    # def get_category_expenses(self, category: str, month: int = None):
    #     """Returns total expenses for a specific category, optionally for a given month."""
    #     if month:
    #         return self.monthly_expenses[month][category]
    #     else:
    #         return sum(self.monthly_expenses[m][category] for m in self.monthly_expenses)
    
    
    
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
        
        total = 0.0
        
        if month is not None:
            if category is not None:
                total = self.monthly_expenses[month][category]
            
            else:
                total = sum(self.monthly_expenses[month].values())
        
        else:
            for month_data in self.monthly_expenses.values():
                if category is not None:
                    total += month_data.get(category, 0.0)
                else:
                    total += sum(month_data.values())
        
        return total