import pytest
import datetime
from src.expense import Expense



USER_ID = "testUser"
def test_successful_init():
    description = "Groceries"
    amount = 15.3
    date = datetime.date(2024, 3, 10)
    category = "Food"
    user_id = USER_ID
    
    expense = Expense(description=description, amount=amount, date=date, category=category, user_id=user_id)
    
    assert expense.amount == 15.3
    assert expense.date == datetime.date(2024, 3, 10)
    assert expense.category == "Food"
    assert expense.description == "Groceries" 
    assert expense.user_id == USER_ID
    
    
    

def test_negative_amount_raises_error():
    with pytest.raises(ValueError, match="Amount cannot be negative"):
        Expense(amount=-10, description="test", category="test", date=datetime.date(2024, 10, 3), user_id=USER_ID)
        

def test_invalid_date_type_raises_error():
    with pytest.raises(ValueError, match="Date must be a datetime.date object"):
        Expense(amount=10, description="test", category="test", date="2024-10-03", user_id=USER_ID)
        
def test_print():
    description = "Groceries"
    amount = 15.3
    date = datetime.date(2024, 10, 3)
    category = "Food"
    user_id = USER_ID
    
    expense = Expense(description=description, amount=amount, date=date, category=category, user_id=USER_ID)
    
    assert str(expense) == "| 2024-10-03 - testUser | Groceries | $15.30 | Food |"