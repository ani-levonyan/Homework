# Given two dictionaries, merge them into a new dictionary, excluding any keys
# that start with an underscore.

merged_dict = {k: v for j in [{"abc": 5, "bca": 6, "_asd": 7}, {"abc1": 7, "bca2": 800, "_asd_": 77}]
               for k, v in j.items() if k[0] != "_"}
