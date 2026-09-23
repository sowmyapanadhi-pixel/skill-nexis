#Bank Account Class
# class BankAccount:

#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance = self.balance + amount
#         print("Amount deposited successfully!")
#         print("Current Balance:", self.balance)

#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance = self.balance - amount
#             print("Amount withdrawn successfully!")
#             print("Current Balance:", self.balance)
#         else:
#             print("Insufficient balance!")

#     def display_balance(self):
#         print("Account Holder:", self.name)
#         print("Current Balance:", self.balance)


# # Create account
# account = BankAccount("Sowmya", 5000)

# # Display balance
# account.display_balance()

# # Deposit
# account.deposit(2000)

# # Withdraw
# account.withdraw(1000)

# # Display final balance
# account.display_balance()

#Library Management System

class Library:

    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print("Book added successfully!")

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print("Book removed successfully!")
        else:
            print("Book not found!")

    def issue_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print("Book issued successfully!")
        else:
            print("Book is not available!")

    def return_book(self, book):
        self.books.append(book)
        print("Book returned successfully!")

    def display_books(self):
        if len(self.books) == 0:
            print("No books available.")
        else:
            print("\nAvailable Books:")
            for book in self.books:
                print("-", book)


# Create library object
library = Library()

# Add books
library.add_book("Python Programming")
library.add_book("Java Programming")
library.add_book("Data Structures")

# Display books
library.display_books()

# Issue a book
library.issue_book("Python Programming")

# Display books
library.display_books()

# Return the book
library.return_book("Python Programming")

# Display books
library.display_books()

# Remove a book
library.remove_book("Java Programming")

# Display final books
library.display_books()


#Calculator Class with Exception Handling

class Calculator:

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return "Cannot divide by zero!"


# Create calculator object
calculator = Calculator()

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    print("\nChoose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Result:", calculator.add(num1, num2))

    elif choice == "2":
        print("Result:", calculator.subtract(num1, num2))

    elif choice == "3":
        print("Result:", calculator.multiply(num1, num2))

    elif choice == "4":
        print("Result:", calculator.divide(num1, num2))

    else:
        print("Invalid choice!")

except ValueError:
    print("Please enter numbers only!")