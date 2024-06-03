# Given the salaries of three employees working at a department, find the
# amount of money by which the salary of the highest-paid employee differs
# from the salary of the lowest-paid employee. The input consists of three
# positive integers - the salaries of the employees. Output a single number,
# the difference between the top and the bottom salaries

first_employee_salary = highest_salary = lowest_salary = int(input("Enter the salary: "))
second_employee_salary = int(input("Enter the salary: "))
third_employee_salary = int(input("Enter the salary: "))

if second_employee_salary > highest_salary:
    highest_salary = second_employee_salary
elif second_employee_salary < lowest_salary:
    lowest_salary = second_employee_salary

if third_employee_salary > highest_salary:
    highest_salary = third_employee_salary
elif third_employee_salary < lowest_salary:
    lowest_salary = third_employee_salary

print(highest_salary - lowest_salary)
