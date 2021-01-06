def loop(x,y):
# x is the number it reaches, y is the increment
    i = 0
    numbers = []

    for i in range(0,x,y):
    #changed from while loop
        print(f"At the top i is {i}")
        numbers.append(i)

        # i = i + y
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")


    print("The numbers: ")

    for num in numbers:
        print(num)


loop(20,2)

'''
when switched from while loop to for loop
the incremental segment is no longer necessary
the increments increase by one naturally
the question is, how do i make the increments increase by two or three?
use the range function
'''
