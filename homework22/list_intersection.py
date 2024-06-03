# Write a function that takes two lists and returns a new list containing only the common
# elements. (without using set)

def list_intersection(inp_list_1: list, inp_list_2: list) -> list:
    common_elements = []
    for i in inp_list_2:
        if i in inp_list_1 and i not in common_elements:
            common_elements.append(i)
    return common_elements


print(list_intersection([1, 2, 3, 4, 7, 10], [1, 2, 4, 5, 8, 9]))
