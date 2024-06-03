# Write a program to check if two strings are balanced. For example, strings s1 and
# s2 are balanced if all the characters in the s1 are present in s2. The character’s
# position doesn’t matter.

s1 = "Ynf"
s2 = "PYnative"
mid_str = ""
output = 1

for j in s2:
    mid_str = mid_str + "-" + str(ord(j))

for i in s1:
    if str(ord(i)) not in mid_str:
        output = output * 0

if output == 0:
    print("False")
else:
    print("True")
