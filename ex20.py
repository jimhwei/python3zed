from sys import argv

script, input_file = argv

def print_all(f):
	print(f.read())

#this function sets file location to 0
def rewind(f):
    f.seek(0)

#prints the linecount(variable), read file line
def print_a_line(line_count, f):
    print(line_count, f.readline(), end = '')
    #no trailing comma in python 3, use end = '' as third parameter

current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

#the current line function is an iterative one
current_line = 1
print_a_line(current_line, current_file)

#current line now 2
current_line += 1
print_a_line(current_line, current_file)

#current line now 3
current_line += 1
print_a_line(current_line, current_file)