# ATM Withdrawal Program
name = input("Enter your name: ")
balance = int(input("Enter your account balance: "))
print("\nWelcome", name)
print("Your current balance is:", balance)
while True:
    amount = int(input("\nEnter withdrawal amount (multiple of 100): "))
    # Check multiple of 100
if amount % 100 != 0:
        print("Please enter the amount in multiples of 100")
        continue
    # Check sufficient balance