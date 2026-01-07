import sys

if len(sys.argv) != 5:
    print("Usage: python employee.py <name> <id> <department> <monthly_salary>")
    sys.exit(1)

employee_name = sys.argv[1]
employee_id = sys.argv[2]
department = sys.argv[3]
monthly_salary = float(sys.argv[4])

annual_salary = monthly_salary * 12

if annual_salary >= 1200000:
    performance = "Excellent"
elif annual_salary >= 800000:
    performance = "Very Good"
elif annual_salary >= 500000:
    performance = "Good"
elif annual_salary >= 300000:
    performance = "Average"
else:
    performance = "Poor"

print(f"Employee Name: {employee_name}")
print(f"Employee ID: {employee_id}")
print(f"Department: {department}")
print(f"Annual Salary: {annual_salary}")
print(f"Performance: {performance}")
