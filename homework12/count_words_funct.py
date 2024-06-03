# Write a function that counts the number of words in a sentence.

def func_count_words_in_sentence(sentence: str) -> int:
    return len(sentence.split(" "))


print(func_count_words_in_sentence("Hello world again!"))
