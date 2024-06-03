# Write a python function which create dict from 2 lists with the same length.

def two_lists_to_dict(inp_list_1, inp_list_2):
    sample_dict = {}
    i = 0
    while i < len(inp_list_1):
        sample_dict[inp_list_1[i]] = inp_list_2[i]
        i += 1
    return sample_dict


print(two_lists_to_dict(["Class1", "Class2", "Class3"], [5, 12, 8]))
