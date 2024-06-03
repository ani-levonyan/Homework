#  Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If
# the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string
# is less than 3, leave it unchanged.

inp_string = input()
if len(inp_string) >= 3:
    if inp_string[-3:] == 'ing':
        inp_string = inp_string + "ly"
    else:
        inp_string = inp_string + "ing"
print(inp_string)
