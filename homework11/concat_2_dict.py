# Write a python program which concat 2 dicts.

def concat_two_dict(inp_dict1, inp_dict2):
    for i in inp_dict2:
        inp_dict1[i] = inp_dict2[i]
    return inp_dict1


print(concat_two_dict({"a": 5, "b": 2}, {"r": 2, "k": 1, "d": 1}))
