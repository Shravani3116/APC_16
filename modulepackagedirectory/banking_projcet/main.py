from banking.account import create_account, check_balance
from banking.transaction import deposit, withdraw
from banking.loan import calculate_loan

name = input("Enter name: ")
account_no = input("Enter account number: ")
balance = float(input("Enter initial balance: "))

account = create_account(name, account_no, balance)

print("Initial Balance:", check_balance(account))

amount = float(input("Enter deposit amount: "))
deposit(account, amount)

amount = float(input("Enter withdrawal amount: "))
withdraw(account, amount)

print("Final Balance:", check_balance(account))

principal = float(input("Enter loan amount: "))
rate = float(input("Enter interest rate: "))
years = int(input("Enter loan duration: "))

interest, total = calculate_loan(principal, rate, years)

print("Loan Interest:", interest)
print("Total Loan Amount:", total)