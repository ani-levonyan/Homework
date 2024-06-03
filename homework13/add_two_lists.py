# Write a Python program to add two given lists using map and lambda.

inp_list_1 = [1, 2, 3]
inp_list_2 = [4, 5, 6]
add_to_list = map(lambda x, y: x + y, inp_list_1, inp_list_2)

print(list(add_to_list))
