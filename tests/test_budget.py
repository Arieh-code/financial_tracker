import pytest 
import datetime
from src.expense import Expense
from src.budget import Budget

def test_set_limit():
    budget = Budget()
    budget.set_limit("Food", 100.0)
    assert budget.limits["Food"] == 100.0
    
    with pytest.raises(ValueError, match="Limit cannot be negative"):
        budget.set_limit("Shopping", -5.2)
        

def test_add_expense():
    budget = Budget()
    expense1 = Expense(10.0, "Food", "Burger", "User123")
    budget.add_expense(expense1)
    
    assert len(budget.expenses[datetime.date.today().month]) == 1
    
    
    expense2 = Expense(15.0, "Food", "Pizza", "User123")
    budget.add_expense(expense2)
    assert len(budget.expenses[datetime.date.today().month]) == 2   
    
    
def test_get_expense():
    
    budget = Budget()
    expense1 = Expense(10.0, "Food", "Burger", "User321", date=datetime.date(2024, 3, 1))
    expense2 = Expense(25.3, "Restaurant", "Kazan", "User321" )
    budget.add_expense(expense1)
    budget.add_expense(expense2)
    
    assert budget.get_expenses() == 35.3
    
    assert budget.get_expenses(month=11) == 25.3
    
    assert budget.get_expenses(category="Food") == 10.0
    

def test_check_limit():
    budget = Budget()
    budget.set_limit("Food", 100.0)
    expense1 = Expense(description="Dinner", amount=90.0, category="Food", user_id="User123")
    budget.add_expense(expense1)
    print("limits:", budget.limits)
    warnings = budget.check_limits()
    print(warnings)
    assert "approaching its limit" in warnings[0]

    expense2 = Expense(description="Lunch", amount=20.0, category="Food", user_id="User123")
    budget.add_expense(expense2)
    warnings = budget.check_limits()
    assert "exceeded its limit" in warnings[0]