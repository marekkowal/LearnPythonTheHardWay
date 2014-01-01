__author__ = 'marek'


## Animal is-a object
class Animal(object):
    def printme(self):
        print "I am an animal!"


## Dog is-a Animal
class Dog(Animal):
    def __init__(self, name):
        ## get the object attribute name and set it to name
        self.name = name
    def printmetoo(self):
        print "I am a dog!"

## Cat is-a Animal
class Cat(Animal):
    def __init__(self, name):
        ## get the object attribute name and set it to name
        self.name = name


## Person is-a object
class Person(object):
    def __init__(self, name):
        ## get the object attribute name and set it to name
        self.name = name

        ## Person has a pet of some kind
        self.pet = None


## Employee is-a Person
class Employee(Person):
    def __init__(self, name, salary):
        ## run the init method of the parent class
        super(Employee, self).__init__(name)
        ## Employee has a salary
        self.salary = salary


## Fish is-a object
class Fish(object):
    pass


## Salmon is-a Fish
class Salmon(Fish):
    pass


## Halibut is-a Fish
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

## mary has-a Pet, satan
mary.pet = satan

## frank is-a Employee
frank = Employee("Frank", 120000)

## frank has-a Pet, rover
frank.pet = rover

## flipper is-a Fish
flipper = Fish()

## crouse is-a Salmon
crouse = Salmon()

## harry is a Halibut
harry = Halibut()

rover.printme()
rover.printmetoo()