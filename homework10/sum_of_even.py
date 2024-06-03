# Write a Python program that calculates the sum of all even numbers between 1 and 100
# using a while loop.

sum_result = 0
i = 0

while i <= 100:
    i += 1
    if i % 2 == 0:
        sum_result += i

print(f"The sum of all even numbers between 1 and 100 is {sum_result}.")
