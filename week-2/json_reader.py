import json

# Open JSON file
with open("students.json", "r") as file:
    data = json.load(file) 

# Print formatted output
for student, details in data.items():
    print("Student:", student)
    print("Name:", details["name"])
    print("Roll Number:", details["roll_number"])
    print("Marks:", details["marks"])
    print("--------------------")