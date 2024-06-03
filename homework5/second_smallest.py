# Write a Python program to find the second smallest number in a list.

inp_list = [5, 7, 3, 9, 11]

if len(inp_list) < 2:
    pass
smallest_number = float('inf')
second_smallest_number = float('inf')

for x in inp_list:
    if x <= smallest_number:
        second_smallest_number = smallest_number
        smallest_number = x
    elif x < second_smallest_number and x != smallest_number:
        second_smallest_number = x
if second_smallest_number == float('inf'):
    pass
else:
    print(second_smallest_number)
