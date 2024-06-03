# Write a Python program to print the floating numbers up to 2 decimal places
# (number must be not greater than 10)

n = input()
if float(n) <= 10.0:
    print(n[:4])
