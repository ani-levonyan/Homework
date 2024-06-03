# Write a Python script that reads a text file (input.txt) and counts the
# occurrences of each character (including spaces and punctuation). Output the
# character frequency to another text file (output.txt).

with open("input.txt", "r") as file:
    text = file.read()
    sample_dict = {}
    for i in text:
        if i not in sample_dict:
            sample_dict[i] = 1
        else:
            sample_dict[i] += 1

with open("output.txt", "x") as file:
    file.write(str(sample_dict))
    