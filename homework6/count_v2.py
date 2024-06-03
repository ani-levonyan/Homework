# Count all letters, digits, and special symbols from a given string.

inp_str = "P@#yn26at^&i5ve"

count_char = 0
count_digit = 0

for i in inp_str:
    if 65 <= ord(i) <= 90 or 97 <= ord(i) <= 122:
        count_char = count_char + 1
    if 48 <= ord(i) <= 57:
        count_digit = count_digit + 1

print("Number of chars is ", count_char, ", number of digits is ", count_digit, ", number of symbol is ",
      len(inp_str) - count_char - count_digit)
