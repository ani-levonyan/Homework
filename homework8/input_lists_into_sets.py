# You are given three lists, list1, list2, and list3. Your task is to implement a
# program that takes these lists and prints the following:

list1 = ["name", "surnames", "age", "phone number"]
list2 = ["name", "middle name", "age", "alternative phone number"]
list3 = ["name", "passport number", "age", "phone number"]

set1 = set(list1)
set2 = set(list2)
set3 = set(list3)

print(f"The set of elements that are common to all three lists is: {set1 & set2 & set3}."
      f"\nThe set of elements that are present in at least two of the three lists, but not in all three is: "
      f"{((set1 & set2) - set3) | ((set1 & set3) - set2) | ((set2 & set3) - set1)}."
      f"\nThe set of elements that are unique to each list (present in only one list) is: {(set1 - (set2 | set3)) |
                                                                                           (set2 - (set1 | set3)) | 
                                                                                           (set3 - (set1 | set2))}.")
