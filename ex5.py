# -*- coding: utf-8 -*-
"""
Created on Sun May  3 22:06:50 2020

@author: jimwe
"""
name = 'jim'
age = 25
height = 182 #cm
inches = round(height * 0.393700787,0)
weight = 75 #kg
pounds = round((weight * 2.2),1)
eyes = "brown"
teeth = "white"
hair = "dark brown"

print("Let's talk about %s." % name)
print(f"He's {inches} inches tall.")
print("He's %d lbs heavy." % pounds)
print("No that heavy")
print("He's got %s eyes and %s hair." % (eyes, hair))
print("His teeth are usually %s depending on the coffee." % teeth)

print ("If I add %d, %d, and %d I get %d." % (
        age, height, weight, age + height + weight))