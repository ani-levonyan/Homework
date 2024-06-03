#  Given a list of words, create a dictionary where keys are words, and values are
# their lengths, but only for words with lengths greater than 3.

dict_1 = {x: len(x) for x in ["asdasdasd", "abcdef", "abc"] if len(x) > 3}
