
with open('meow.txt', 'w') as file:
    file.write("1\n")
    file.write("hello\n")

with open('meow.txt', 'r') as file:
    contents = file.read()
    print(contents)
