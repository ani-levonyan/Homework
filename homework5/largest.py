# Write a Python program to get the largest number from a list.

inp_list = [5, 7, 3, 9, 11]
largest_number = inp_list[0]

for x in inp_list:
    if x >= largest_number:
        largest_number = x

print(largest_number)
