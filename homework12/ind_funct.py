# Write a function that finds the index of a given element in a list. If the element is not
# present, return -1.

def funct_index(giv_element, inp_list):
    if giv_element in inp_list:
        return inp_list.index(giv_element)
    return -1


print(funct_index(2, [1, 0, 5, 4]))
