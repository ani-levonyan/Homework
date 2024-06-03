# Write a program to check if two strings are balanced. For example, strings s1 and
# s2 are balanced if all the characters in the s1 are present in s2. The character’s
# position doesn’t matter.

s1 = "Ynf"
s2 = "PYnative"
check = 1

for i in s1:
    if i in s2:
        check = check * 1
    else:
        check = check * 0

if check == 1:
    print("True")
else:
    print("False")
