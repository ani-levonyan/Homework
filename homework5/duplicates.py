# Write a Python program to remove duplicates from a list.

inp_list = [25, 1, 1, 13]
trial_list = []
for x in inp_list:
    if x not in trial_list:
        trial_list.append(x)

print(trial_list)
