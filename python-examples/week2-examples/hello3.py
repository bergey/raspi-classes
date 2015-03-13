# Example of loops and conditionals

name = ''
while name == '' or not str.isalpha(name[0]):
    print("What is your name?")
    name = input()
print("Hello {}".format(name))
