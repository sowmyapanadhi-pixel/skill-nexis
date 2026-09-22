#Temperature Converter
def celsius_to_fahrenheit():
    temperature_c=float(input("Enter Temperature in Celsius:"))
    fahrenheit=(temperature_c*9/5)+32
    return fahrenheit
def fahrenheit_to_celsius():
    temperature_f=float(input("Enter temperature in Fahrenheit:"))
    celsius=(temperature_f-32)*5/9
    return celsius
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
choice=int(input("Enter your choice:"))
if choice==1:
    print("Temperature in Fahrenheit:",celsius_to_fahrenheit())
elif choice==2:
    print("Temperature in Celsius:",fahrenheit_to_celsius())
else:
    print("Invalid choice")
print("Thank you for using the temperature converter!")


#Student Grade Calculator

def calculate_grade():
    marks1 = float(input("Enter your marks 1:"))
    marks2 = float(input("Enter your marks 2:"))
    marks3 = float(input("Enter your marks 3:"))
    total_marks = marks1 + marks2 + marks3
    average_marks = total_marks / 3

    if average_marks >= 90:
        grade = "A"
    elif average_marks >= 80:
        grade = "B"
    elif average_marks >= 70:
        grade = "C"
    elif average_marks >= 60:
        grade = "D"
    else:
        grade = "F"

    return average_marks, grade

average, grade = calculate_grade()
print("Average Marks:", average)
print("Grade:", grade)


#Even/Odd + Prime Number Checker

number=int(input("Enter a number:"))
if number%2==0:
    print("The number is Even")
else:
    print("The number is Odd")
if number <= 1:
    is_prime = False
else:
    is_prime = True

    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break
if is_prime:
    print("The number is Prime")
else:
    print("The number is Not Prime")
