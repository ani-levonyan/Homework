# Write a function that checks if two sets are disjoint (have no common elements).

def disjoint_sets(input_set_1: set, input_set_2: set) -> bool:
    ans = False
    if input_set_1 & input_set_2 == set():
        ans = True
    return ans


print(disjoint_sets({5, 4,  3, 2}, {1, 8, 7, 6}))
