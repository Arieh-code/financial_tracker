from src.expense import Expense
from src.budget import Budget
from src.notifier import Notifier
import datetime
import argparse



def main():
    
    parser = argparse.ArgumentParser(description="CLI Financial tracker")
    parser.add_argument("--user_id", type=str, required=True, help="The current userID")
    subparser = parser.add_subparsers(dest="command")
    
    # command add expense
    add_expense_parser = subparser.add_parser("add-expense", help="Add a new expense")
    add_expense_parser.add_argument("--amount", type=float, required=True, help="Amount spent")
    add_expense_parser.add_argument("--category", type=str, required=True, help="Expense category")
    add_expense_parser.add_argument("--date", type=str, help="Date of the expense (YYYY-MM-DD)")
    add_expense_parser.add_argument("--description", type=str, required=True, help="Expense description")
    # add_expense_parser.add_argument("--user_id", type=str, required=True, help="The user of the expense")
    
    
    # command Set limit
    set_limit_parser = subparser.add_parser("set-limit", help="set a spending limit for a category")
    set_limit_parser.add_argument("--category", type=str, required=True, help="Category of the expense")
    set_limit_parser.add_argument("--amount", type=float, required=True, help="The limit")
    
    
    # command view summary
    view_summary_parser = subparser.add_parser("view-summary", help="view total expense")
    view_summary_parser.add_argument("--month", type=int, help="Month to filter (1-12)")
    view_summary_parser.add_argument("--category", type=str, help="Category to filter")
    
    
    # command start notifier
    start_notifier_parser = subparser.add_parser("start-notifier", help="start the budget notifier")
    
    
    # command stop notifier
    stop_notifier_parser = subparser.add_parser("stop-notifier", help="stop budget notifier")
    
    
    # parse arguments
    args = parser.parse_args()
    
    if args.user_id is None:
        print("Please provide a user_id")
        return
    
    # instantiate budget and notifier with user_id
    budget = Budget(args.user_id)
    notifier = Notifier(budget)
    
      
    if args.command == "add-expense":
        date = datetime.datetime.strptime(args.date, "%Y-%m-%d") if args.date else datetime.datetime.now()
        expense = Expense(amount=args.amount, category=args.category, description=args.description, user_id=args.user_id, date=date)
        budget.add_expense(expense)
        print(f"Added expense: {expense}")

    
        budget.set_limit(category=args.category, amount=args.amount)
        print(f"Set limit: {args.category} - {args.amount}")
        
    
    elif args.command == "view-summary":
        total = budget.get_expenses(month=args.month, category=args.category)
        print(f"Total expenses: {total}")
        
    
    elif args.command == "start-notifier":
        notifier.start()
        print("Notifier started, you will receive budget limit warnings\n")


    elif args.command == "stop-notifier":
        notifier.stop()
        print("Notifier stop, you will not receive alerts or warnings")
    
    else:
        parser.print_help()
        
    
if __name__ == "__main__":
    main()