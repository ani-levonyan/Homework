# Write a python function, which add a new value with given key in dict.

def add_key_to_dict(k, v, inp_dict):
    inp_dict[k] = v
    return inp_dict


print(add_key_to_dict("a", 5, {"b": 2, "r": 2}))
