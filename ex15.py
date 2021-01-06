#import module from sys dictionary
from sys import argv

#setting up param
script, filename = argv, input("file name: ")

#text open fxn
txt = open(filename)

#printing file name
print("Here's your file %r:" % filename)
print(txt.read())
#above is reading a text file

#prompting to open file again
print("Type the filename again:")
file_again = input("> ")

#opening file fxn
txt_again = open(file_again)

#reading file fxn
print(txt_again.read())

txt.close()
txt_again.close()