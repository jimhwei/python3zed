ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(' ')
#changed ten_things into a list called stuff, based on space
#call split on ten_things
more_stuff = ["Day", "Night", "Song", "Frisbee",
                "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    #takes last thing on more_stuff
    #call popon more stuff
    print("Adding: ", next_one)
    stuff.append(next_one)
    #appends it to stuff
    print(f"There are {len(stuff)} items now.")
    #display length of stuff
    #loops until 10 items in list

print("There we go: ", stuff)

print("Let's do some things with stuff. ")

print(stuff[1])
print(stuff[-1]) # whoah! fancy
print(stuff.pop())
print(' '.join(stuff)) # what? cool!
#joins the list items into one large text string, not stored
print("#".join(stuff[3:6])) # super stellar
#joins items on list with #, essentially replaces space with #
    #not stored

"""
things that would be in a real life list:
groceries, store inventory, deck of cards, gps coordinates,
list of books,
"""
