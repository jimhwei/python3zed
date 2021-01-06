def add(a,b):
    print(f"ADDING {a} + {b}")
    return a + b

def subtract(a,b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply(a,b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a,b):
    print(f"DIVIDING {a} / {b}")
    return a / b

print("Let's do some math with just functions!")

age = add(30, -3.14)
height = subtract(78, 4.4)
weight = multiply(0.1,2)
iq = divide(100, 1.5)
#note variables always start lower case
#upper case should be a method

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

# A puzzle for the extra credit, type it in anyway.
print("Here is a puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
print("That becomes: ", what, "Can you do it by hand?")
#74-(50/2*180)+35

def kfc():
    return "let's eat kfc"
chicken = kfc()
print(chicken)

dont = add(age,2)**add(height,2)
print("Don't you open up that window:", dont)

print(2 + 34 / 100 - 1023)
