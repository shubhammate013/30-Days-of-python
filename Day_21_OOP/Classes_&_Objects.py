## Classes and Objects

# Python is an object oriented programming language. Everything in Python is an object, with its properties and methods. A number, string, list, dictionary, tuple, set etc. used in a program is an object of a corresponding built-in class. We create class to create an object. A class is like an object constructor, or a "blueprint" for creating objects. We instantiate a class to create an object. The class defines attributes and the behavior of the object, while the object, on the other hand, represents the class.

# We have been working with classes and objects right from the beginning of this challenge unknowingly. Every element in a Python program is an object of a class.
# Let us check if everything in python is a class:

num = 10
type(num)     # <class 'int'>

string = 'string'
type(string)     # <class 'str'>

boolean = True
type(boolean)   #<class 'bool'>

lst = []
type(lst)     #<class 'list'>

tpl = ()
type(tpl)     #<class 'tuple'>

set1 = set()
type(set1)    # <class 'set'>

dct = {}
type(dct)     # <class 'dict'>


### Creating a Class

# To create a class we need the key word **class** followed by the name and colon. Class name should be **CamelCase**.


# syntax
'''
class ClassName:
  code goes here
'''

# **Example:**

class Person:
  pass
print(Person)        # <__main__.Person object at 0x10804e510>

### Creating an Object

# We can create an object by calling the class.

p = Person()
print(p)

### Class Constructor

# In the examples above, we have created an object from the Person class. However, a class without a constructor is not really useful in real applications. Let us use constructor function to make our class more useful. Like the constructor function in Java or JavaScript, Python has also a built-in **__init__**() constructor function. The **__init__** constructor function has self parameter which is a reference to the current instance of the class
# **Examples:**

class Person:
      def __init__ (self, name):
        # self allows to attach parameter to the class
          self.name =name

p = Person('Shubham')
print(p.name)
print(p)

# output
# Shubham
# <__main__.Person object at 0x2abf46907e80>


# Let us add more parameters to the constructor function.

class Person:
      def __init__(self, firstname, lastname, age, country, city):
          self.firstname = firstname
          self.lastname = lastname
          self.age = age
          self.country = country
          self.city = city


p = Person('Memory', 'Reboot', 250, 'Russia', 'Moscow')
print(p.firstname)
print(p.lastname)
print(p.age)
print(p.country)
print(p.city)


# output
'''
Memory
Reboot 
250
Russia
Moscow

'''

### Object Methods

# Objects can have methods. The methods are functions which belong to the object.

# **Example:**

class Person:
      def __init__(self, firstname, lastname, age, country, city):
          self.firstname = firstname
          self.lastname = lastname
          self.age = age
          self.country = country
          self.city = city
      def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}'

p = Person('Deavy', 'Jones', 250, 'Finland', 'Helsinki')
print(p.person_info())

# output
'''
Deavy Jones is 250 years old. He lives in Helsinki, Finland
'''

### Object Default Methods

# Sometimes, you may want to have a default values for your object methods. If we give default values for the parameters in the constructor, we can avoid errors when we call or instantiate our class without parameters. Let's see how it looks:

# **Example:**

class Person:
      def __init__(self, firstname='Gojo', lastname='Saturo', age=250, country='Japan', city='Shibuya'):
          self.firstname = firstname
          self.lastname = lastname
          self.age = age
          self.country = country
          self.city = city

      def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}.'

p1 = Person()
print(p1.person_info())
p2 = Person('John', 'Doe', 30, 'Austrelia', 'Sydney')
print(p2.person_info())

# output
'''
Gojo Saturo is 250 years old. He lives in Shibuya, Japan.
John Doe is 30 years old. He lives in Sudney, Asutrelia.
'''

