# Write a function that removes an element at a specified index from a list. Handle the
# IndexError by raising a custom exception if the index is out of range.

def list_element_removal(input_list: list, input_index: int) -> list:
    if input_index >= len(input_list):
        raise IndexError("Index is out of range.")
    input_list.remove(input_list[input_index])
    return input_list


print(list_element_removal([0, 4, "abc", [4, 3, 7]], 4))
