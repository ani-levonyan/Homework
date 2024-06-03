# Write a Python program that takes two sets as input and returns a new set containing
# elements that are present in the first set but not in the second set.

sample_set1 = {"name", "surname", "age", "phone number"}
sample_set2 = {"name", "middle name", "age", "alternative phone number"}

result = sample_set1 - sample_set2

print(result)
