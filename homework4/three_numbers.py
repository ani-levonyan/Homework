# Input three integers. Output the word “Sorted” if the numbers are listed in
# a non-increasing or non-decreasing order and “Unsorted” otherwise.

first_integer = int(input())
second_integer = int(input())
third_integer = int(input())

if first_integer <= second_integer <= third_integer or first_integer >= second_integer >= third_integer:
    print("Sorted")
else:
    print("Unsorted")
