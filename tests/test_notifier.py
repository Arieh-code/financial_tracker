import time
from src.budget import Budget
from src.notifier import Notifier
from src.expense import Expense
from unittest.mock import patch


def test_notifier_start_stop():
    budget = Budget()
    notifier = Notifier(budget, interval=1)

    # Start the notifier and ensure it is running
    notifier.start()
    assert notifier.running == True

    # Stop the notifier and ensure it is no longer running
    notifier.stop()
    assert notifier.running == False



@patch('src.budget.Budget.check_limits', return_value=["Warning: Test warning"])
def test_notifier_check_limits(mock_check_limits):
    budget = Budget()
    notifier = Notifier(budget, interval=1)
    
    # Start the notifier
    notifier.start()
    time.sleep(2)  # Allow it to run briefly

    # Stop the notifier and check if check_limits was called
    notifier.stop()
    assert mock_check_limits.called
