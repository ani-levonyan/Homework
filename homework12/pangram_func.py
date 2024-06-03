# Write a function that checks if a sentence is a pangram.

def pangram_funct(sentence: str) -> bool:
    sample_list = []
    sentence = set(sentence.lower())
    for i in range(97, 123):
        sample_list.append(chr(i))
    for j in sample_list:
        if j not in sentence:
            return False
    return True


print(pangram_funct("The quick brown fox jumps over the lazy dog"))
