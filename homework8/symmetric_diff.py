# Write a Python program that takes two sets as input and returns a new set containing
# elements that are present in either of the input sets, but not in both.

sample_set1 = {"name", "surname", "age", "phone number"}
sample_set2 = {"name", "middle name", "age", "alternative phone number"}

result = sample_set2 ^ sample_set1

print(result)
