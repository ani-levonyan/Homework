# Write a Python program that calculates the Fibonacci sequence up to a given number n
# using a while loop. The Fibonacci sequence is a series of numbers where each number
# is the sum of the two preceding ones.

inp_num = int(input())
n = 1
fin_list = [0, 1]

while n < inp_num:
    fin_list.append(int(fin_list[n]) + int(fin_list[n-1]))
    n += 1

print(fin_list)
