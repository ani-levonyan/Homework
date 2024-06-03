# Write a function that prompts the user to enter a number and tries to convert it to an
# integer. Handle the TypeError exception by printing a message indicating that the input
# is not a valid number. Use a finally block to print "Type conversion process completed."

def convert_type(inp):
    try:
        output = int(inp)
        return output
    except ValueError:
        print("Value Error. Input is not a valid number.")
    finally:
        print("Type conversion process completed.")


print(convert_type("abc"))
