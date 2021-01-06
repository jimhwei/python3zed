# -*- coding: utf-8 -*-
"""
Created on Mon May  4 07:44:53 2020

@author: jimwe
"""
#setting the variable
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

#printing x & y
print (x)
print (y)

#print a formatted string with x & y
print ("I said: %r." % x)
print ("I also said: '%s'." % y)

#setting variables, hilarious is boolean and joke_eval to be formatted
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

#combinging variables and printing
print (joke_evaluation % hilarious)

#printing two strings one after another
w = "This is the left side of..."
e = "a string with a right side"

print (w + e)