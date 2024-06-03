# Write a function that finds the index of a given element in a list. If the element is not
# present, return -1.

def funct_index(giv_element, inp_list):
    for i in range(0, len(inp_list)):
        if inp_list[i] == giv_element:
            return i
    return -1


print(funct_index(4, [1, 2, 5, 4]))
