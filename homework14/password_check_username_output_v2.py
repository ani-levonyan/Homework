input_pass = input("Please enter the password: ")

with open("../../02_Classwork/username_pass.txt", "r") as file:
    text = file.read().replace("\n", ", ").replace(": ", ", ").split(", ")
    if input_pass in text:
        for i in range(1, len(text), 2):
            if text[i] == input_pass:
                print(text[i-1])
    else:
        print("User not found")
