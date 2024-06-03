# Write a Python program that asks the user to enter a password. Keep asking for the
# password until the correct password "secret" is entered. Provide appropriate feedback
# to the user.

corr_pass = "secret"
input_pass = input("Please enter the password: ")

while input_pass != corr_pass:
    input_pass = input("Wrong password.\nPlease enter the password: ")

if input_pass == corr_pass:
    print("Correct password. Access granted.")
