# Input two positive integers, and output a line describing their relation.
# Follow the sample format.

a = input()
b = input()

if int(a) == int(b):
    print(a + " = " + b)
elif int(a) < int(b):
    print(a + " < " + b)
else:
    print(a + " > " + b)
