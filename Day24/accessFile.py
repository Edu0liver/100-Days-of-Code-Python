with open("./Day24/my_file.txt") as file:
    contents = file.read()
    print(contents)
    file.close()

with open("./Day24/my_file2.txt", mode="w") as file:
    file.write("New text.")

with open("./Day24/my_file.txt", mode="a") as file:
    file.write("\nNew text.")