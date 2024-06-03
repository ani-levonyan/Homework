# Write a Python program to find intersection of two given arrays using Lambda.

inp_list_1 = [1, 2, 3, 5, 7, 8, 9, 10]
inp_list_2 = [1, 2, 4, 8, 9]

intersection_function = list(filter(lambda x: x in inp_list_1, inp_list_2))

print(list(intersection_function))
