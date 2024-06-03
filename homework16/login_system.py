# Write a simple login system where the user enters a username and password. Handle
# the KeyError by raising a custom exception if the username is not found in the users
# database(dictionary).

input_username = input("Please enter the username: ")
input_pass = input("Please enter the password: ")

fin_dict = {"username1": "password1", "username2": "password2", "username3": "password3"}

if input_username in fin_dict:
    while fin_dict[input_username] != input_pass:
        input_pass = input("Wrong password.\nPlease enter the password: ")
    else:
        print("Access granted.")
else:
    raise KeyError("User not found")
