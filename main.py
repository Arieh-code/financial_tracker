from src.expense import Expense
import datetime
def main():
    
    # Create a sample expense
    expense = Expense(
        amount=50.0,
        category="Food",
        date=datetime.date.today(),
        description="Groceries",
        user_id="user123"
    )

    # Save the expense to MongoDB
    expense.save_to_db()


if __name__ == "__main__":
    main()