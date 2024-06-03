# Write a Python function to get a string made of its first three characters of a specified string. If
# the length of the string is less than 3 then return the original string.

def first_three_char():
    inp_string = input()
    if len(inp_string) >= 3:
        inp_string = inp_string[:3]
    print(inp_string)


first_three_char()
