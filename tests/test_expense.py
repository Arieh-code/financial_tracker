import pytest
import datetime
from src.expense import Expense

def test_successful_init():
    description = "Groceries"
    amount = 15.3
    date = datetime.date(2024, 3, 10)
    category = "Food"
    
    expense = Expense(description=description, amount=amount, date=date, category=category)
    
    assert expense.amount == 15.3
    assert expense.date == datetime.date(2024, 3, 10)
    assert expense.category == "Food"
    assert expense.description == "Groceries" 
    
    
    

def test_negative_amount_raises_error():
    with pytest.raises(ValueError, match="Amount cannot be negative"):
        Expense(amount=-10, description="test", category="test", date=datetime.date(2024, 10, 3))
        

def test_invalid_date_type_raises_error():
    with pytest.raises(ValueError, match="Date must be a datetime.date object"):
        Expense(amount=10, description="test", category="test", date="2024-10-03")
        
def test_print():
    description = "Groceries"
    amount = 15.3
    date = datetime.date(2024, 10, 3)
    category = "Food"
    
    expense = Expense(description=description, amount=amount, date=date, category=category)
    
    assert str(expense) == "Groceries | $15.30 | 2024-10-03 | Food"