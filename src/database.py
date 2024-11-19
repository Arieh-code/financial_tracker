from pymongo import MongoClient
import os


try:
    client = MongoClient("mongodb://localhost:27017/")
    db = client["financial_tracker"]
except Exception as e:
    print("Error connecting to MongoDB:", e)
    raise


def insert_expense(expense_data):
    """Insert an expense document into the MongoDB collection."""
    db["expenses"].insert_one(expense_data)


def get_expenses_by_user(user_id):
    """Retrieve all expenses for a given user_id."""
    return list(db["expenses"].find({"user_id": user_id}))



def delete_expense(expense_id):
    """Delete an expense by its unique ID."""
    db["expenses"].delete_one({"_id": expense_id})
    
    
def set_limit(user_id, category, amount):
    """Inserts into DB the limits of a category"""
    db["limits"].update_one(
        {"user_id": user_id, "category": category},
        {"$set": {"amount": amount}},
        upsert=True
    )
    

def get_limits_by_user(user_id):
    """Retrieves the limits set by user_id"""
    return list(db["limits"].find({"user_id": user_id}))
    
    
