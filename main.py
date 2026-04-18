from operations.operations import *

def menu():
    print("\n===== ATM MENU =====")
    print("1. Display Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Show Statement")
    print("5. Exit")

while True:
    menu()
    choice = input("Enter your choice: ")

    if choice == '1':
        display_balance()

    elif choice == '2':
        deposit_money()

    elif choice == '3':
        withdraw_money()

    elif choice == '4':
        show_statement()

    elif choice == '5':
        print("Thank you for using ATM")
        break

    else:
        print("Invalid choice, try again")