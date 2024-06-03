# Write a python function, which create a dictionary for given number N, where keys are numbers from
# 1 to N, and values are cubs of that numbers.

def new_dict_num_and_cube(n):
    sample_dict = {}
    i = 1
    while i <= n:
        sample_dict[i] = i ** 3
        i += 1
    return sample_dict


print(new_dict_num_and_cube(5))
