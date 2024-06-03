# Implement a Python program that reads a text file (input.txt), prompts the user
# for a word to find, and another word to replace it with. Replace all occurrences of
# the first word with the second word and save the modified text to a new file
# (output.txt).

inp_string_find = input("Please enter the word to find and replace: ")
inp_string_replace = input("Please enter the word to replace the first with: ")

with open("input.txt", "r") as file:
    text = file.read()
    if inp_string_find in text:
        text = text.replace(inp_string_find, inp_string_replace)

with open("output.txt", "x") as file:
    file.write(text)
