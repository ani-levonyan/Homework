# Write a function that checks the length of a string provided by the user. Handle the
# TypeError by raising a custom exception if the input is not a string.

def string_length_check(input_string: str) -> str:
    if not isinstance(input_string, str):
        raise TypeError("Only strings are allowed.")
    return f"The length of the input string is {len(input_string)}"


print(string_length_check(543))
