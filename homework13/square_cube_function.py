# Write a Python program to square and cube every number in a given list of integers using Lambda.

inp_numbers = [1, 2, 3, 4, 5]

square_function = list(map(lambda a: a ** 2, inp_numbers))
cube_function = list(map(lambda a: a ** 3, inp_numbers))

print(square_function, cube_function)
