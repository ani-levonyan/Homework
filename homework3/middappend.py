# Append new string in the middle of a given (even number of characters) string

inp_string = input()
new_string = input()
if len(inp_string) % 2 == 0:
    inp_string = inp_string[:int(len(inp_string)/2)] + new_string + inp_string[int(len(inp_string)/2):]
    print(inp_string)
