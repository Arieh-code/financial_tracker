from pymongo import MongoClient
import os

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")  # Adjust this URI if using a remote MongoDB server

# Define the database and collection
db = client["financial_tracker"]
expenses_collection = db["expenses"]


def insert_expense(expense_data):
    """Insert an expense document into the MongoDB collection."""
    expenses_collection.insert_one(expense_data)


def get_expenses_by_user(user_id):
    """Retrieve all expenses for a given user_id."""
    return list(expenses_collection.find({"user_id": user_id}))



def delete_expense(expense_id):
    """Delete an expense by its unique ID."""
    expenses_collection.delete_one({"_id": expense_id})
    
    
