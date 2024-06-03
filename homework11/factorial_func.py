# Write a Python function to calculate the factorial of a number (a non-negative
# integer). The function accepts the number as an argument.

def factorial(num):
    i = 0
    result = 1
    while num - i > 0:
        result = result * (num - i)
        i += 1
    return result


print(factorial(5))
