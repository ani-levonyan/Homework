# Write a Python program to change a given string to a new string where the first and last chars have been exchanged.

inp_string = input()
inp_string = inp_string[-1]+inp_string[1:-1]+inp_string[0]
print(inp_string)
