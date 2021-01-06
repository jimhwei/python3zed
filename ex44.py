"""Most of the uses of inheritance can be simplified or replaced with 
composition, and multiple inheritance should be avoided at all costs.

Inheritance is used to indicate that one class will get 
most or all of its features from a parent class. This
happens implicitly whenever you write class Foo(Bar), 
which says “Make a class Foo that inherits from Bar.” 
When you do this, the language makes any action that you do on 
instances of Foo also work as if they were done to an instance of Bar. 
Doing this lets you put common functionality in the Bar class,
then specialize that functionality in the Foo class as needed."""

#inheritance
class Parent(object):
    
    def override(self):
        print("Parent override()")
    
    def implicit(self):
        print("Parent implicit()")
    
    def altered(self):
        print("Parent altered()")

class Child(Parent):
    
    def override(self):
        print("Child override()")
    
    def altered(self):
        print("Child altered() BEFORE")
        super(Child,self).altered()
        #prints parent.override
        print("Child altered() AFTER")
        
        
dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()

print("-" * 10)

"""'super' alters the behavior of Parent class before or 
after it runs"""

#composition
class Other(object):
    
    def override(self):
        print("Other override()")
    
    def implicit(self):
        print("Other implicit()")
    
    def altered(self):
        print("Other altered()")
        
class Child(object):
    #here there is no is-a relationship
    
    def __init__(self):
        self.other = Other()
        #here we use a has-a relationship
    
    def implicit(self):
        self.other.implicit()
    
    def override(self):
        print("Child override()")
    
    def altered(self):
        print("Child, before Other altered()")
        self.other.altered()
        print("Child, After Other altered()")

son = Child()

son.implicit()
son.override()
son.altered()