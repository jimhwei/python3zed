#define the function
def cheese_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers")
    print("That's enough")
    print("Get a blankey\n")

#give function numbers hard coding
print("We can just give the function numbers directly:")
cheese_crackers(20,30)

#set variables and the pass them in the fxn
print("OR, we can use variables from our script:")
amt_of_cheese = 10
amt_of_crackers = 50

cheese_crackers(amt_of_cheese, amt_of_crackers)

#do math on the inside
print("We can even do math inside too:")
cheese_crackers(10 + 20, 50 +6)

#add values on variables
print("And we can combine the two, variables and math:")
cheese_crackers(amt_of_cheese + 100, amt_of_crackers + 1000)

#Study Drills#
def bbq(wings, ribs, amt_ppl):
    print(f"You have {wings} wings and {ribs} ribs")
    print(f"There are {amt_ppl} guests attending")
    if ribs * 1 + wings * 6 <= amt_ppl * 12:
        print("we don't have enough food!")
    else:
        print("We have enough food")

bbq(100, 10, 5)

amt_wings = 10
amt_ribs = 5
ppl = 10

bbq(amt_wings + 50 * 2, amt_ribs / 2, ppl - 1)
