# CLI Financial Tracker

A Python-based command-line application to track expenses and manage budgets. The tracker supports storing data in a MongoDB database, enabling dynamic retrieval and persistent storage of financial data.

## Features

- Add expenses with details such as amount, category, description, and date.
- Set and manage spending limits for different categories.
- View summaries of expenses by category or month.
- Real-time notifications for approaching or exceeding budget limits (via threading).
- Persistent storage using MongoDB for user-specific data.

## Technologies Used

- **Python 3.10+**
- **MongoDB** (local instance).
- **Pymongo** for MongoDB integration.
- **Argparse** for CLI commands.

## Prerequisites

1. **Python**: Ensure you have Python 3.10 or later installed.
2. **MongoDB**: Install MongoDB locally or configure a connection to a MongoDB Atlas instance.
3. **Pymongo**: Install the required package using pip:
   ```bash
   pip install pymongo
   ```

## Installation, Setup, and Usage

```bash
# Clone the repository
git clone https://github.com/yourusername/financial_tracker.git
cd financial_tracker

# Set up the environment
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
pip install -r requirements.txt

# Start MongoDB locally
mongod

# Usage examples
# Add an Expense
python main.py --user_id test_user add-expense --amount 50 --category "Groceries" --description "Weekly shopping"

# Set a Spending Limit
python main.py --user_id test_user set-limit --category "Groceries" --amount 200

# View Expense Summary
python main.py --user_id test_user view-summary --month 11 --category "Groceries"

# Start the Notifier
python main.py --user_id test_user start-notifier

# Stop the Notifier
python main.py --user_id test_user stop-notifier
```
