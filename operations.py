import data.data as db

def display_balance():
    print(f"\nCurrent Balance: ₹{db.balance}")

def deposit_money():
    amount = int(input("Enter deposit amount: ₹"))
    if amount > 0:
        db.balance += amount
        db.transactions.append(f"Deposited ₹{amount}")
        print("Money deposited successfully")

def withdraw_money():
    amount = int(input("Enter withdraw amount: ₹"))
    if amount <= db.balance:
        db.balance -= amount
        db.transactions.append(f"Withdrawn ₹{amount}")
        print("Money withdrawn successfully")
    else:
        print("Insufficient balance")

def show_statement():
    print("\nTransaction Statement:")
    for t in db.transactions:
        print("-", t)