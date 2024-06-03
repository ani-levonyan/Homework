# Write a function that calculates the sum of squares of numbers from 1 to n.

def sum_squares(n: int) -> int:
    sum_of_sq = 0
    for i in range(1, n+1):
        sum_of_sq += i ** 2
    return sum_of_sq


print(sum_squares(3))
