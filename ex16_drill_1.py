from sys import argv

script, filename = argv

print(f"I'm going to open file {filename}. ")
file_contents = open(filename)

print(f"The contents of file {filename} is :")
print(file_contents.read())

file_contents.close()

print(f"File {filename} has been closed. ")
