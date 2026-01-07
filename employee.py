
# Accept employee details
employee_name = input("Enter Employee Name: ")
employee_id = input("Enter Employee ID: ")
department = input("Enter Department: ")
monthly_salary = float(input("Enter Monthly Salary: "))

# Calculate annual salary
annual_salary = monthly_salary * 12

# Determine performance category
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

# Display employee details
print("\nEmployee Details")
print("----------------")
print("Name:", employee_name)
print("Employee ID:", employee_id)
print("Department:", department)
print("Annual Salary:", annual_salary)
print("Performance Category:", performance)
