# Write a Python script that takes multiple text files as input and concatenates their
# contents into a single text file.

inp_lst = ["input.txt", "username_pass.txt"]

with open("final_file.txt", "x") as file:
    file.write('')

new_file = open("final_file.txt", "a")

for i in inp_lst:
    with open(i, "r") as file:
        text = file.read()
        new_file.write(text)


new_file.close()
