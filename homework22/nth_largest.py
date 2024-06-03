# Write a function that returns the nth largest element from a list.

list_1 = [1, 5, 2, 4, 7, 8, 10, 15, 6]

fin_list = []


def ordered_list(inp_list):
    largest_number = float('-inf')

    while len(inp_list) > 0:
        for number in inp_list:
            if number >= largest_number:
                largest_number = number

        fin_list.append(largest_number)
        inp_list.remove(largest_number)
        ordered_list(inp_list)
    return fin_list


def nth_largest(inp_list: list, n: int) -> int:
    if len(inp_list) < n:
        raise IndexError("Index exceeds ")
    else:
        final_list = ordered_list(inp_list)
        return final_list[n-1]


print(nth_largest(list_1, 3))
