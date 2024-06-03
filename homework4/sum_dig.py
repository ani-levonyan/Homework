# Input a two-digit natural number and output the sum of its digits. You can
# assume that the input will be a two-digit number and need not check that
# programmatically.

two_dig_num = int(input())

print(two_dig_num // 10 + two_dig_num % 10)
