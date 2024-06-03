# Write a function that calculates the average of a list of numbers.

def aver_function(num_list: list) -> float:
    sum_of_num = 0
    if len(num_list) == 0:
        return 0
    else:
        for j in num_list:
            sum_of_num += j
    return sum_of_num/len(num_list)


print(aver_function([2, 3, 4, 5]))
