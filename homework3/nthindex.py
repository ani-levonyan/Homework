# Write a Python program to remove the n-th index character from a nonempty string.

inp_string = input()
n = int(input())
if len(inp_string) >= 1:
    inp_string = inp_string[:n] + inp_string[n+1:]
print(inp_string)
