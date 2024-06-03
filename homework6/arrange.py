# Arrange string characters such that lowercase letters should come first.

# inp_str = input()
inp_str = "PyNaTive"
mid_str = ""

for i in inp_str:
    if i.islower():
        mid_str = mid_str + i
        inp_str = inp_str.replace(i, "")

inp_str = mid_str + inp_str

print(inp_str)
