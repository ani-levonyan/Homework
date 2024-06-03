# Write a Python script that takes multiple text files as input and concatenates their
# contents into a single text file.

def concat_text_files(inp_lst: list):
    with open("final_file.txt", "x") as file:
        file.write('')

    new_file = open("final_file.txt", "a")

    for path in inp_lst:
        with open(path, "r") as file:
            text = file.read()
            new_file.write(text)

    new_file.close()


print(concat_text_files(["input.txt", "username_pass.txt"]))
