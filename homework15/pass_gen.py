import random
import string


def pass_generator(length: int, letters: True, numbers: True, symbols: True):
    components = ''
    password = ''
    if letters:
        components += string.ascii_letters
        password += random.choice(string.ascii_letters)
    if numbers:
        components += string.digits
        password += random.choice(string.digits)
    if symbols:
        components += string.punctuation
        password += random.choice(string.punctuation)
    while length - len(password) > 0:
        password += random.choice(components)
    trial_list = list(password)
    random.shuffle(trial_list)
    password = ''.join(trial_list)
    return f"The suggested password is {password}"


print(pass_generator(8, True, True, True))
