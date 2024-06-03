# Create a string made of the first, middle and last character of given string with odd number of
# symbols

inp_string = input()
if len(inp_string) % 2 != 0:
    inp_string = inp_string[0] + inp_string[int(len(inp_string)/2)] + inp_string[-1]
    print(inp_string)
