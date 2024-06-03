# Write a Python function to find the Max of three numbers.

def max_of_three(num1, num2, num3):
    largest_number = num1
    if num2 >= largest_number:
        largest_number = num2
    if num3 >= largest_number:
        largest_number = num3
    return largest_number


print(max_of_three(5, 11, 3))
