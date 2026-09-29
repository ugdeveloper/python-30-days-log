## Day 21 - 30 days of python challenge

# Classes

# Creating a class (PascalCase)

# syntax

class ClassName:
    # Code goes here
    pass

# Examples

class Person:
    pass
print(Person)

p = Person()
print(p)

# Class constructors

class Person:
    def __init__ (self, name):
        #self allows to attach parameter to the class
        self.name = name

p = Person('Mijo')
print(p.name)
print(p)

# Add some more parameters

class Person:
    def __init__(self, firstname, lastname, age, country, city):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city

p = Person('Mijo', 'Bakalar', 17, 'Canada', 'Toronto')

# Object Methods

class Person:
    def __init__(self, firstname, lastname, age, country, city):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city
    def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}'

p = Person('Mijo', 'Bakalar', 17, 'Canada', 'Toronto')

print(p.personinfo())

# Object Default methods

# can specify default values in the parameters for init function within class

# Mutator functions to modify class values

# Inheritence (interesting)

class Student(Person):
    pass

# Student class inherits all the constructor and functions from the parent class

# In our exampe no init construction is called in the child class, but if we did hav eone we could access the parent functions using the super keywords

    