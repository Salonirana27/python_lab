transaction_amount = float(input("Enter transaction amount: "))
account_age = int(input("Enter account age in months: "))
transaction_type = input("Is the transaction international? (yes/no): ")

# Condition check
if transaction_amount > 200000 and account_age < 6 and transaction_type.lower() == "yes":
    print("⚠ Transaction flagged for MANUAL VERIFICATION")
else:
    print("✅ Transaction is safe")