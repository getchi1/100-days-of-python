# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)
# import os

# with open("my_file.txt", "a") as file:
#     file.write("\nHello World")

# with open("new_file.txt", "a") as file:
#     file.write("New text")

with open("../Day24/my_file.txt") as file: #relative path
    data1 = file.read()
    print(data1)


with open("C:/Users/shett/OneDrive/Desktop/new_file.txt") as file: #using absolute path
    data = file.read()
    print(data)

# print(os.getcwd())

#C:\Users\shett\OneDrive\Desktop\new_file.txt