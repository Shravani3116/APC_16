# 3. Deposits and Withdrawals

file = open("transactions.txt", "r")

total_deposits = 0
total_withdrawals = 0
balance = 0

largest_transaction = 0
largest_type = ""

for line in file:
    data = line.strip().split(",")

    transaction_type = data[0]
    amount = float(data[1])

    if transaction_type == "deposit":
        total_deposits += amount
        balance += amount

    elif transaction_type == "withdrawal":
        total_withdrawals += amount
        balance -= amount

    if amount > largest_transaction:
        largest_transaction = amount
        largest_type = transaction_type

file.close()

print("Total Deposits:", total_deposits)
print("Total Withdrawals:", total_withdrawals)
print("Final Balance:", balance)
print("Largest Transaction:", largest_transaction)
print("Transaction Type:", largest_type)