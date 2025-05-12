print("Welcome to the Expense Splitter 🤑\n")

num_people = int(input("number of people: "))


expenses = {}
for _ in range(num_people):
    name = input("name: ")
    amount = float(input(f"How much did {name} spend? ₹"))
    expenses[name] = amount


total_expense = sum(expenses.values())
equal_share = total_expense / num_people

print(f"\nTotal expense: ₹{total_expense:.2f}")
print(f"Each person should pay: ₹{equal_share:.2f}\n")


for name, amount in expenses.items():
    balance = amount - equal_share
    if balance > 0:
        print(f"{name} should receive ₹{abs(balance):.2f}")
    elif balance < 0:
        print(f"{name} should pay ₹{abs(balance):.2f}")
    else:
        print(f"{name} is settled up ✅")
