# Write a Python function to calculate count of each letter in string.

def count_letters(inp_string):
    sample_dict = {}
    for i in inp_string:
        if i not in sample_dict:
            sample_dict[i] = 1
        else:
            sample_dict[i] += 1
    return sample_dict


print(count_letters("abrakadabra"))
