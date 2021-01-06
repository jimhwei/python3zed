def expensive():
    print("Is it too expensive?")

    choice = input("> ")

    if choice == "yes":
        happiness()
    elif choice == "no":
        cool()
    else:
        print("I didn't understand that")
        expensive()


def happiness():
    print("Can you put a price on happiness?")

    choice = input("> ")

    if choice == "yes":
        partner()
    elif choice == "no":
        cool()
    else:
        print("I didn't understand that")
        partner()


def partner():
    print("Is this about what your partner will say?")

    choice = input("> ")

    if choice == "yes":
        love()
    elif choice == "no":
        cool()
    else:
        print("I didn't understand that")
        partner()


def love():
    print("Do they love you?")

    choice = input("> ")

    if choice == "no":
        cool()
    if choice == "yes":
        happy()
    else:
        print("What?")
        love()


def happy():
    print("So they want you to be happy?")

    choice = input("> ")

    if choice == "yes":
        cool()
    else:
        find()


def find():
    print("Do you want to find a partner?")

    choice = input("> ")

    if choice == "yes":
        cool()
    else:
        alone()

def alone():
    print("Do you want to die alone?")

    choice = input("> ")

    if choice == "yes":
        die()
    elif choice == "no":
        find()
    else:
        alone()


def die():
    print("Do you want to die alone happily?")

    choice = input("> ")

    if choice == "yes":
        cool()
    elif choice == "no":
        print("Buy a car")
    else:
        die()


def cool():
    print("Cool! Buy the bike")


def fool():
    print("It's 'Yes' or 'No' fool! Try again")
    exit(0)


def start():
    print("Are you going to buy the bike?")

    choice = input("> ")

    if choice == "yes":
        cool()
    elif choice == "no":
        expensive()
    else:
        fool()

start()
