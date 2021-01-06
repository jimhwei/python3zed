## Animal is-a object (look at extra credit)
class Animal(object):
    pass

## Class dog is-a animal
class Dog(Animal):

        def __init__(self, name):
            ##__init__ has-a name
            self.name = name

## class cat is-a animal
class Cat(Animal):

    def __init__(self, name):
        ## __init__ has-a name
        self.name = name

## class Person is-a object
class Person(object):

    def __init__(self, name):
        ## __init__ has a name
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## class Employee is-a person
class Employee(Person):

    def __init__(self, name, salary):
        ## ?? hmm what is this strange magic? (has-a class
            #name and salary param)
        super(Employee, self).__init__(name)
        ## salary has-a salary called salary
        self.salary = salary

## class fish is-a object
class Fish(object):
    pass

## class salmon is-a fish
class Salmon(Fish):
    pass

## class salmon is-a fish
class Halibut(Fish):
    pass


## rover is-a instance of class dog has-a name Rover
rover = Dog("Rover")

## satan is-a instance of cat that is-a Satan
satan = Cat("Satan")

## mary is-an instant of person that is-a mary
mary = Person("Mary")

## mary has-a attribute that is-a satan
mary.pet = satan

## frank is-a employee with 120000
frank = Employee("Frank", 120000)

## pet from frank is-a roer
frank.pet = rover

## flipper is-an instance of class fish
flipper = Fish()

## crouse is-an instance of salmon
crouse = Salmon()

## harry is- an istance of fish salmon
harry = Halibut()
