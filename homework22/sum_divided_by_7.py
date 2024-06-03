# Given a list of numbers, write a function to find the sum of all numbers in the list that
# can be divided by 7.

def sum_funct(inp_list: list) -> int:
    fin_sum = 0
    for i in inp_list:
        if i % 7 == 0:
            fin_sum += i
    return fin_sum


print(sum_funct([1, 7, 14, 2, 7]))
