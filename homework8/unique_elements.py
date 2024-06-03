# Write a Python program that takes two sets as input and returns a new set containing all
# unique elements from both input sets.

sample_set1 = {"name", "surname", "age", "phone number"}
sample_set2 = {"name", "middle name", "age", "alternative phone number"}

result = sample_set1 | sample_set2

print(result)
