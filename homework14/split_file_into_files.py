# Develop a Python Function that reads a large text file (input.txt) and splits it
# into smaller files, each containing a specified number of lines. Function paramis
# ter the number of lines per file. Generate multiple output files (output1.txt,
# output2.txt, etc.)

def split_file_into_mult_file(input_file, numbers_of_lines_in_file):
    with open(input_file, "r") as file:
        lines_of_original_file = file.readlines()

    number_of_files = (len(lines_of_original_file) // numbers_of_lines_in_file) + int((len(lines_of_original_file) % numbers_of_lines_in_file) + 0.5)

    for file_index in range(number_of_files):
        output = f"output{file_index + 1}.txt"
        with open(output, "w") as file:
            start_row = file_index * numbers_of_lines_in_file
            end_row = (file_index + 1) * numbers_of_lines_in_file
            file.writelines(lines_of_original_file[start_row:end_row])


split_file_into_mult_file("input.txt", 20)
