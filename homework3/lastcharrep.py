# Write a Python function to get a string made of 4 copies of the last two characters of a
# specified string (length must be at least 2).

def char_rep():
    inp_string = input()
    if len(inp_string) >= 2:
        inp_string = inp_string[-2:] * 4
        print(inp_string)


char_rep()
