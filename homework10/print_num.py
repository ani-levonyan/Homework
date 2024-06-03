# Write a Python program that prompts the user to enter a positive integer and then prints
# all the numbers from 1 to that number using a while loop.

inp_num = int(input("Enter a positive integer: "))
i = 1

while i <= inp_num:
    print(i)
    i += 1
