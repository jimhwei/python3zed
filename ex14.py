from sys import argv

script, user_name = argv#, "jim"
prompt = '> '

print("Hi %s, I'm the %script." % (user_name,script))
print("I'd like to ask you a few questions.")
print("Do you like me %s?" % user_name)
likes = input(prompt)

print("Where do you live %s?" % user_name)
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print("How old are you?")
age = input(prompt)
'''
print("""
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
You are %r years old. That's old!
"""% (likes, lives, computer, age))
'''

#python 3 string formatting
print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
You are {age} years old. That's old!
""")

#Difference is that the response has no quotation marks in python 3