from sys import argv # import models

script, filename = argv # unpackage argv

txt = open(filename) # open the file and give it to txt variable

print(f"Here's your file {filename}:") # print filename
print(txt.read()) # print cotend of the file

print("Type the filename again:") # prompt message
file_again = input("> ") # get filename from imput()

txt_again = open(file_again) #reopen the file and give the stream obj to txt_again

print(txt_again.read()) # print content of the file
