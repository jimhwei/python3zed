people = 20
cats = 30
dogs = 15


if people < cats:
    print("Too many cats! The world is doomed!")

if people > cats:
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")

if people > dogs:
    print("The world is dry!")


dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs:
    print("People are less than or equal to dogs.")


if people == dogs:
    print("People are dogs")

dogs += 100
if dogs > cats and people:
    print("It's a dog's world")

#1. the if statements checks the boolean logic underneath
#2. these are the clauses of the if arguments, similar to function args
#3. python compiler throws an error message, indent required
#4. see dog's world
#5. then you'd have to redo the math and see if boolean logic holds t/f
