# Bank Transaction Analyzer

transactions = list(map(float, input("Enter transactions separated by space: ").split()))

balance = sum(transactions)

withdrawals = [t for t in transactions if t < 0]
largest_withdrawal = min(withdrawals) if withdrawals else 0

large_deposits = len([t for t in transactions if t > 10000])

print("Total Balance:", balance)
print("Largest Withdrawal:", largest_withdrawal)
print("Deposits > ₹10000:", large_deposits)

#output
"""Enter transactions separated by space: 10000 -2000 15000 -5000 8000
Total Balance: 26000.0
Largest Withdrawal: -5000.0
Deposits > ₹10000: 1"""