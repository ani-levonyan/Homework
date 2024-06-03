# Write a function that finds the key with the maximum value in a dictionary.

dict_1 = {"abc": 12, "bca": 15, "cda": 20, "efg": 10, "lmn": 24}


def max_key(inp_dict: dict) -> str:
    maximum_key = None
    maximum_value = float('-inf')
    for key, value in inp_dict.items():
        if value > maximum_value:
            maximum_value = value
            maximum_key = key
    return maximum_key


print(max_key(dict_1))
