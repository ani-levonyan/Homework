# Write a Python program to get the smallest number from a list.

inp_list = [5, 7, 3, 9, 11]
smallest_number = inp_list[0]

for x in inp_list:
    if x <= smallest_number:
        smallest_number = x

print(smallest_number)
