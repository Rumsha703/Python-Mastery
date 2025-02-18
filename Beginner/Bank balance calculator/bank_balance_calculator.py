transactions=[500,-250,500,-250]


balance=0
for transaction in transactions:
    if transaction > 0:
        balance += transaction
        print(f"User has been credited ${transaction}")
    else:
        balance -= transaction
        print(f"User has been debited ${transaction}")

print(f"User's total balance is ${balance}")
    
