# Print a square pattern using a nested for loop. The pattern should have 5 rows and 5
# columns.

x = ""

for i in range(1, 6):
    for j in range(1, 6):
        x = j * "* "
        if len(x) == 5:
            x = ""
            break
    print(x)
