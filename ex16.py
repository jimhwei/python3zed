# -*- coding: utf-8 -*-
"""
Created on Fri May  8 09:45:07 2020

@author: jimwe
"""

from sys import argv

script, filename = argv

print("We're going to erase %r." % filename)
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')
#the 'w' used is to be explicit

'''#you have to be careful with this function
print("Truncating the file. Goodbye!")
target.truncate()'''
#truncate fxn is not necessary as open with 'w'
#explicityl tells you it's going to overwrite it

print("Now I'm going to ask you for three lines.")
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

target.write("%r\n%r\n%r\n" %(line1, line2,line3))

'''
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
'''

print("And finally, we close it.")
target.close()

txt = open(filename)
print("Here's your file %r:" % filename)
print(txt.read())