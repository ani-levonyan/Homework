# Write a function that performs the following tasks:
# Accepts a list and an index as input.
# Attempts to access the element at the given index in the list.
# Handles both IndexError
# Uses a finally block to print "Task completed" regardless of whether an exception
# occurred or not.

def get_element(inp_list: list, n: int):
    try:
        element = inp_list[n]
        print(f"The element at {n}-th position is {element}")
    except IndexError as e:
        print(e)
    finally:
        print("Task completed")


get_element(["Hello", 1, "world", 8, [1, 2, 3, 4]], 8)
