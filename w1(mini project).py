#Simple ATM Simulator
balance = 5000
correct_pin = "1234"
def check_balance():
    print("Current balance:", balance)
def deposit():
    amount = float(input("Enter amount to deposit: "))
    global balance
    balance += amount
    print("Amount deposited:", amount)
    print("New Balance:", balance)
def withdraw():
    amount = float(input("Enter amount to withdraw: "))
    global balance
    if amount > balance:
        print("Insufficient balance")
    else:
        balance -= amount
        print("Amount withdrawn:", amount)
        print("Remaining Balance:", balance)

pin = input("Enter your PIN: ")
if pin == correct_pin:
    print("Login successful")
    while True:
        print("\nATM Menu:")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            check_balance()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
else:
    print("Incorrect PIN")