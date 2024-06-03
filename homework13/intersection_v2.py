# Write a Python program to find intersection of two given arrays using Lambda.

intersection_function = lambda inp_list_1, inp_list_2: set(inp_list_1) & set(inp_list_2)

print(list(intersection_function([1, 2, 3, 5, 7, 8, 9, 10], [1, 2, 4, 8, 9])))
