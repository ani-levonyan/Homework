# Write a function that swaps the values of two tuples.

def tuple_swap(tuple_1: tuple, tuple_2: tuple) -> tuple:
    tuple_1, tuple_2 = tuple_2, tuple_1
    return tuple_1, tuple_2


print(tuple_swap((1, 2, 3, 4), (1, 5, 8, 7)))
