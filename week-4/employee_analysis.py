import pandas as pd

# Load CSV file
df = pd.read_csv("employee_data.csv")

print("----- EMPLOYEE DATA -----")
print(df)


# Calculate average salary
average_salary = df["Salary"].mean()

print("\nAverage Salary:", average_salary)


# Count employees by department
department_count = df["Department"].value_counts()

print("\n----- EMPLOYEES BY DEPARTMENT -----")
print(department_count)


# Filter employees above salary threshold
salary_threshold = 60000

high_salary = df[df["Salary"] > salary_threshold]

print("\n----- EMPLOYEES ABOVE", salary_threshold, "-----")
print(high_salary)


# Export filtered results to a new CSV
high_salary.to_csv("high_salary_employees.csv", index=False)

print("\nFiltered employee data saved successfully!")