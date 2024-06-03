# Print a right-angled triangle pattern using a nested for loop. The pattern should have 5 rows.

x = ""

for i in range(1, 6):
    for j in range(1, i+1):
        x = j * "* "
    print(x)
