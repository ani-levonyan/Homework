# Print the multiplication table of 5 using a for loop and f”strings”. The table should be
# printed up to 10.

inp_num = 5
inp_range = range(1, 11)

for i in inp_range:
    print(f"{inp_num} * {i} = {inp_num * i}")
